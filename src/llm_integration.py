"""
Integración con OpenRouter API para análisis de CVs.
"""

import os
from typing import Optional

from dotenv import load_dotenv
from openrouter import OpenRouter

from prompt_templates import SYSTEM_PROMPT, create_cv_analysis_prompt

# Cargar variables de entorno
load_dotenv()

# Precios de Gemini 3.1 Flash Lite en OpenRouter (USD por millón de tokens)
PRICE_INPUT_PER_M = 0.10
PRICE_OUTPUT_PER_M = 0.40


def calculate_cost(prompt_tokens: int, completion_tokens: int) -> float:
    """
    Calcula el coste estimado de una llamada al LLM.

    Args:
        prompt_tokens: Tokens consumidos en el prompt (entrada)
        completion_tokens: Tokens generados en la respuesta (salida)

    Returns:
        Coste estimado en USD
    """
    cost_input = (prompt_tokens / 1_000_000) * PRICE_INPUT_PER_M
    cost_output = (completion_tokens / 1_000_000) * PRICE_OUTPUT_PER_M
    return round(cost_input + cost_output, 8)


class CVAnalyzer:
    """Cliente para analizar CVs usando OpenRouter API."""

    def __init__(self):
        """Inicializa el cliente de OpenRouter."""
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        self.model_name = os.getenv("MODEL_NAME", "gemini-3.1-flash-lite")

        if not self.api_key:
            raise ValueError(
                "OPENROUTER_API_KEY no encontrada. Por favor, configura tu archivo .env"
            )

        self.client = OpenRouter(api_key=self.api_key)

    def analyze_cv(
        self, cv_text: str, sector: str, puesto: str, experiencia: int
    ) -> dict:
        """
        Analiza un CV usando el LLM.

        Args:
            cv_text: Texto del CV a analizar
            sector: Sector profesional objetivo
            puesto: Puesto al que aspira
            experiencia: Años de experiencia

        Returns:
            Diccionario con:
                - content (str): Respuesta del LLM
                - prompt_tokens (int): Tokens de entrada consumidos
                - completion_tokens (int): Tokens de salida generados
                - total_tokens (int): Total de tokens
                - cost_usd (float): Coste estimado en USD

        Raises:
            Exception: Si hay error en la llamada a la API
        """
        try:
            # Crear el prompt con el contexto
            user_prompt = create_cv_analysis_prompt(
                cv_text, sector, puesto, experiencia
            )

            # Llamar a la API de OpenRouter
            with OpenRouter(api_key=self.api_key) as client:
                response = client.chat.send(
                    model=self.model_name,
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": user_prompt},
                    ],
                    temperature=0.2,  # Bajo para output JSON estructurado y determinista
                    max_tokens=3000,  # Suficiente para análisis detallado
                    top_p=0.85,  # Nucleus sampling conservador para tareas estructuradas
                )

            # Extraer datos de uso de tokens
            usage = getattr(response, "usage", None)
            prompt_tokens = getattr(usage, "prompt_tokens", 0) if usage else 0
            completion_tokens = getattr(usage, "completion_tokens", 0) if usage else 0
            total_tokens = (
                getattr(usage, "total_tokens", prompt_tokens + completion_tokens)
                if usage
                else 0
            )
            cost_usd = calculate_cost(prompt_tokens, completion_tokens)

            return {
                "content": response.choices[0].message.content,
                "prompt_tokens": prompt_tokens,
                "completion_tokens": completion_tokens,
                "total_tokens": total_tokens,
                "cost_usd": cost_usd,
            }

        except Exception as e:
            raise Exception(f"Error al llamar a OpenRouter API: {str(e)}")

    def test_connection(self) -> bool:
        """
        Prueba la conexión con OpenRouter API.

        Returns:
            True si la conexión es exitosa, False en caso contrario
        """
        try:
            with OpenRouter(api_key=self.api_key) as client:
                client.chat.send(
                    model=self.model_name,
                    messages=[
                        {"role": "user", "content": "Hello"},
                    ],
                    max_tokens=10,
                )
            return True
        except Exception:
            return False
