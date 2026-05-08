"""
Parseadores para procesar y estructurar el output del LLM.
"""

import json
import re
from typing import Any, Dict, Optional


def extract_json_from_text(text: str) -> Optional[str]:
    """
    Extrae un objeto JSON de un texto que puede contener contenido adicional.

    Args:
        text: Texto que contiene JSON

    Returns:
        String con el JSON extraído o None si no se encuentra
    """
    # Intentar encontrar JSON entre ```json y ```
    json_pattern = r"```json\s*(\{.*?\})\s*```"
    match = re.search(json_pattern, text, re.DOTALL)
    if match:
        return match.group(1)

    # Intentar encontrar JSON entre ``` y ```
    json_pattern = r"```\s*(\{.*?\})\s*```"
    match = re.search(json_pattern, text, re.DOTALL)
    if match:
        return match.group(1)

    # Intentar encontrar JSON en el texto directamente
    json_pattern = r"\{.*\}"
    match = re.search(json_pattern, text, re.DOTALL)
    if match:
        return match.group(0)

    return None


def parse_cv_analysis(llm_output: str) -> Optional[Dict[str, Any]]:
    """
    Parsea el output del LLM y lo convierte en estructura de datos.

    Args:
        llm_output: Respuesta cruda del LLM

    Returns:
        Diccionario con el análisis parseado o None si falla el parseo
    """
    try:
        # Intentar parsear directamente
        return json.loads(llm_output)
    except json.JSONDecodeError:
        pass

    # Intentar extraer JSON del texto
    json_str = extract_json_from_text(llm_output)
    if json_str:
        try:
            return json.loads(json_str)
        except json.JSONDecodeError:
            pass

    return None


def validate_cv_analysis(analysis: Dict[str, Any]) -> bool:
    """
    Valida que el análisis tenga la estructura esperada.

    Args:
        analysis: Diccionario con el análisis

    Returns:
        True si la estructura es válida, False en caso contrario
    """
    required_keys = [
        "puntuacion_general",
        "resumen_general",
        "analisis_secciones",
        "fortalezas_principales",
        "areas_mejora",
        "mejoras_sugeridas",
    ]

    # Verificar claves principales
    for key in required_keys:
        if key not in analysis:
            return False

    # Verificar que analisis_secciones tenga las secciones esperadas
    secciones = analysis.get("analisis_secciones", {})
    if not isinstance(secciones, dict):
        return False

    # Verificar que las listas no estén vacías
    if not analysis.get("fortalezas_principales"):
        return False
    if not analysis.get("areas_mejora"):
        return False
    if not analysis.get("mejoras_sugeridas"):
        return False

    return True


def get_fallback_analysis() -> Dict[str, Any]:
    """
    Proporciona un análisis de fallback en caso de error de parseo.

    Returns:
        Diccionario con análisis básico de fallback
    """
    return {
        "puntuacion_general": 0,
        "resumen_general": "No se pudo analizar el CV correctamente. Por favor, intenta de nuevo.",
        "analisis_secciones": {},
        "fortalezas_principales": [
            "No se pudo completar el análisis. Por favor, verifica el formato del CV."
        ],
        "areas_mejora": [
            "No se pudo completar el análisis. Por favor, intenta nuevamente."
        ],
        "mejoras_sugeridas": [
            "Verifica que el CV esté en formato legible (PDF, DOCX o TXT)",
            "Asegúrate de que el archivo no esté corrupto",
            "Intenta subir el archivo nuevamente",
        ],
        "seccion_mejorada": {
            "nombre_seccion": "N/A",
            "version_original": "No disponible",
            "version_mejorada": "No disponible",
        },
    }
