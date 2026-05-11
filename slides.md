<p align="center">
  <img src="logoURVppd.png" alt="Fundació URV" height="70"/>
</p>

# CV Assistant AI — Reto 9
### Asistente de revisión y mejora de CVs con IA Generativa

**Artificial Intelligence Foundations** | Fundació URV | Mayo 2026

---

## Diapositiva 1 — Portada

<p align="center">
  <img src="logoURVppd.png" alt="Fundació URV" height="60"/>
</p>

# 🎯 CV Assistant AI
### Asistente inteligente de revisión y mejora de CVs

**Reto 9 — IA Generativa**
Artificial Intelligence Foundations | Fundació URV | Mayo 2026

---

## Diapositiva 2 — El Problema

### ¿Por qué los buenos profesionales no consiguen entrevistas?

- ⏱️ **6–10 segundos**: tiempo medio de un recruiter en revisar un CV
- 💸 **Feedback profesional** de RRHH es costoso y no siempre accesible
- 📄 Un CV mal estructurado descarta candidatos con independencia de su valía

### Nuestra solución

> Democratizar el acceso al feedback experto sobre CVs mediante IA Generativa:
> **análisis profundo, en segundos, de forma gratuita.**

---

## Diapositiva 3 — Demo en Vivo

### 🚀 Demostración

*(Aquí se realiza la demo en vivo de la aplicación)*

**Flujo a mostrar**:
1. Configurar sidebar: sector Tecnología · puesto "Senior Developer" · 5 años
2. Subir `test_cv_example.txt`
3. Pulsar "Analizar CV" → spinner → resultados
4. Recorrer: puntuación general → análisis por secciones → sugerencias → sección mejorada
5. Mostrar botón de descarga JSON

---

## Diapositiva 4 — Arquitectura de la Solución

### Stack tecnológico

```text
Usuario → Streamlit UI → CVAnalyzer → OpenRouter API (Gemini 3.1 Flash Lite)
                                ↓
                          parsers.py → Visualización Streamlit
```

| Capa | Tecnología | Rol |
|---|---|---|
| Frontend | Streamlit | UI, upload, visualización |
| LLM | Gemini 3.1 Flash Lite (OpenRouter) | Análisis del CV |
| Extracción PDF | PyPDF2 | Lectura de texto de archivos PDF |
| Extracción DOCX | python-docx | Lectura de archivos Word |
| Parseo | parsers.py | Extracción JSON + 3 niveles de fallback |
| Prompting | prompt_templates.py | 7 técnicas de PE |
| Despliegue | Streamlit Community Cloud | Hosting gratuito desde GitHub |

---

## Diapositiva 5 — Decisiones Técnicas Clave

### ¿Por qué estas tecnologías y no otras?

| Decisión | Elegido | Descartado | Razón |
|---|---|---|---|
| **Framework UI** | Streamlit | FastAPI+React, Gradio | Python puro, componentes nativos, despliegue integrado |
| **Modelo LLM** | Gemini 3.1 Flash Lite | Llama 3.1 70B (Groq), GPT-3.5 | Groq deprecated el modelo; OpenAI requiere tarjeta |
| **API de LLM** | OpenRouter | Groq, OpenAI direct | Gratuito (500 req/día), compatible con SDK OpenAI |
| **Despliegue** | Streamlit Cloud | Heroku, AWS, Railway | Gratuito, nativo para Streamlit, secrets integrados |
| **Parseo** | 3 niveles de fallback | json.loads() simple | El LLM se desvía ocasionalmente; fallback evita errores |

### Decisión más crítica: temperatura 0.2

> Reducir temperatura de **0.7 → 0.2** eliminó prácticamente todos los fallos de parseo JSON
> → Coherencia y determinismo por encima de creatividad en tareas estructuradas

---

## Diapositiva 6 — Prompt Engineering (1/2)

### Técnicas aplicadas y su impacto

| Técnica | Impacto medido |
|---|---|
| **Role Prompting** | Calibra vocabulario y criterios de RRHH |
| **Context Setting** | Relativiza puntuación según perfil del candidato |
| **Chain-of-Thought** | Coherencia entre los 8 campos del JSON |
| **Output Schema JSON** | Elimina campos renombrados y tipos erróneos |

**Ejemplo — Role Prompting**:

```text
SYSTEM: "Eres un experto senior en recursos humanos y revisión de CVs
con más de 15 años de experiencia. Siempre proporcionas respuestas
ÚNICAMENTE en formato JSON válido."
```

---

## Diapositiva 7 — Prompt Engineering (2/2)

### Técnicas aplicadas y su impacto (continuación)

| Técnica | Impacto medido |
|---|---|
| **Few-Shot Examples (×3)** | Calibra escala 0–10 en bajo/medio/alto, evita benevolencia del modelo |
| **Instrucciones Negativas** | Elimina JSON envuelto en markdown, decimales, datos inventados |
| **Separación de datos** | Previene prompt injection desde el CV |
| **Temperature = 0.2** | Reduce fallos de parseo de ~30% a <5% |

**Ejemplo — Instrucción Negativa**:

```text
CRÍTICO: Devuelve ÚNICAMENTE el objeto JSON.
Cero texto antes ni después. No uses bloques ```json.
Si el JSON no puede parsearse directamente, tu respuesta es inválida.
```

---

## Diapositiva 8 — Parseo y Mapeo del Output

### Requisito del reto: NO mostrar texto crudo

**Sistema de parseo de 3 niveles** (`parsers.py`):

```
Respuesta del LLM
      ↓
1. json.loads() directo         → ✅ éxito → mapear a Streamlit
      ↓ fallo
2. Regex: extraer bloque ```json``` → ✅ éxito → mapear a Streamlit
      ↓ fallo
3. Regex: extraer { ... }       → ✅ éxito → mapear a Streamlit
      ↓ fallo
4. get_fallback_analysis()      → análisis básico de error
```

**Mapeo del JSON a componentes Streamlit**:
- `puntuacion_general` → `st.metric`
- `analisis_secciones` → `st.expander` × 3
- `fortalezas_principales` → `st.success` (lista)
- `seccion_mejorada` → `st.text_area` comparativa (original vs mejorada)

---

## Diapositiva 9 — Resultados y Validación

### Ejemplo de análisis real

**CV analizado**: perfil de data scientist con 3 años de experiencia, sector Tecnología

| Campo | Valor obtenido |
|---|---|
| Puntuación general | 6/10 |
| Puntuación Experiencia | 7/10 |
| Puntuación Educación | 8/10 |
| Puntuación Habilidades | 4/10 |
| Nº sugerencias generadas | 6 |

**Observación**: Sin few-shot examples, el modelo puntuaba este mismo CV con 8/10. Los examples calibraron la escala y generaron sugerencias 3× más concretas.

---

## Diapositiva 10 — Conclusiones

### Lo que aprendimos

✅ **El prompt engineering es tan importante como el modelo**
→ La calidad del output depende más del diseño del prompt que del tamaño del modelo

✅ **Temperature baja = JSON consistente**
→ Reducir de 0.7 a 0.2 eliminó prácticamente todos los fallos de parseo

✅ **Few-shot examples calibran la escala**
→ Sin ejemplos, el modelo era excesivamente benevolente

✅ **El parseo robusto es obligatorio en producción**
→ El LLM se desvía del formato ocasionalmente; el fallback es imprescindible

### Trabajo futuro
- Comparación CV vs ofertas reales de empleo (LinkedIn/Indeed API)
- Soporte multilingüe
- OCR para CVs escaneados

---

## Diapositiva 11 — Cierre

# ¡Gracias!

### 🔗 Links del proyecto

- **App en Streamlit**: https://cv-assistant-ai-ynjx6qsnd6prgwq3m4dipz.streamlit.app/
- **Repositorio GitHub**: https://github.com/jamarcas1984/cv-assistant-ai
- **Vídeo demo**: `[enlace en video.txt]`

### ❓ Preguntas

---

<p align="center">
  <img src="logoURVppd.png" alt="Fundació URV" height="50"/>
  <br/>
  <em>Artificial Intelligence Foundations | Fundació Universitat Rovira i Virgili | Mayo 2026</em>
</p>
