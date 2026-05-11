---
marp: true
theme: default
paginate: true
backgroundColor: #ffffff
style: |
  section {
    font-family: 'Segoe UI', Arial, sans-serif;
    font-size: 22px;
    color: #1a1a2e;
    padding: 40px 60px;
  }
  section.cover {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    color: #ffffff;
    text-align: center;
    justify-content: center;
  }
  section.cover h1 {
    font-size: 54px;
    color: #0055a0;
    margin-bottom: 10px;
  }
  section.cover h3 {
    color: #98a9ee;
    font-weight: 400;
    font-size: 24px;
  }
  section.cover p {
    color: #8892b0;
    font-size: 18px;
    margin-top: 30px;
  }
  section.cover .badge {
    display: inline-block;
    background: #0055a0;
    color: white;
    padding: 6px 18px;
    border-radius: 20px;
    font-size: 24px;
    margin-top: 16px;
  }
  h1 {
    color: #0f3460;
    font-size: 36px;
    border-bottom: 3px solid #0055a0;
    padding-bottom: 10px;
    margin-bottom: 20px;
  }
  h2 {
    color: #0f3460;
    font-size: 30px;
  }
  h3 {
    color: #0055a0;
    font-size: 24px;
  }
  table {
    font-size: 17px;
    width: 100%;
    border-collapse: collapse;
  }
  th {
    background: #0f3460;
    color: white;
    padding: 8px 12px;
  }
  td {
    padding: 7px 12px;
    border-bottom: 1px solid #ddd;
  }
  tr:nth-child(even) td {
    background: #f4f6fb;
  }
  code {
    background: #f4f6fb;
    color: #ffff;
    padding: 2px 6px;
    border-radius: 4px;
    font-size: 16px;
  }
  pre {
    background: #1a1a2e;
    color: #6e95a3;
    font-size: 15px;
    padding: 16px 20px;
    border-radius: 8px;
    border-left: 4px solid #0055a0;
  }
  blockquote {
    border-left: 4px solid #0055a0;
    background: #f4f6fb;
    padding: 10px 20px;
    margin: 16px 0;
    border-radius: 0 8px 8px 0;
    font-style: italic;
    color: #333;
  }
  ul li {
    margin: 6px 0;
  }
  .columns {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 30px;
  }
  .highlight {
    background: #fff3cd;
    border-left: 4px solid #ffc107;
    padding: 10px 16px;
    border-radius: 0 8px 8px 0;
    margin: 10px 0;
  }
  section.section-divider {
    background: linear-gradient(135deg, #0f3460 0%, #16213e 100%);
    color: white;
    text-align: center;
    justify-content: center;
  }
  section.section-divider h1 {
    color: #0055a0;
    border: none;
    font-size: 46px;
  }
  section.section-divider p {
    color: #a8b2d8;
    font-size: 22px;
  }
  footer {
    font-size: 13px;
    color: #8892b0;
  }
  section.thanks {
    background: linear-gradient(135deg, #1a1a2e 0%, #0f3460 100%);
    color: black;
    text-align: center;
    justify-content: center;
  }
  section.thanks h1 {
    color: #0055a0;
    font-size: 60px;
    border: none;
  }
  section.thanks a {
    color: #a8d8ea;
  }
  section.thanks p {
    color: #e0e6f0;
  }
  section.thanks a strong {
    color: #0055a0;
  }
---

<!-- _class: cover -->
<!-- _paginate: false -->
<!-- _footer: "Javier Martín Castro · Reto 9 — IA Generativa · Artificial Intelligence Foundations · Fundació URV · Mayo 2026" -->

![height:96](logoURVppd.png)

# 🔎 CV Assistant AI

## Asistente inteligente de revisión y mejora de CVs

<br>

**Reto 9 — IA Generativa**

<span class="badge">**Artificial Intelligence Foundations · Fundació URV · Mayo 2026**</span>

---

<!-- _footer: "Reto 9 — CV Assistant AI · Fundació URV · Mayo 2026" -->

# ¿Por qué un revisor de CVs con IA?

### El problema real

<div class="columns">
<div>

#### 👤 El candidato

- Invierte horas elaborando su CV
- No tiene acceso fácil a feedback profesional
- Un CV mal estructurado → descartado en segundos

#### 💸 El coste del feedback experto

- Coach de carrera: **60–150 € / sesión**
- No siempre accesible para todos los perfiles

</div>
<div>

#### ⏱️ El lado del recruiter

> Los recruiters dedican una media de **6–10 segundos** a la revisión inicial de un CV

- Priorizan estructura clara y logros cuantificables
- CVs sin palabras clave del sector → descartados automáticamente

#### 🎯 La oportunidad

Acceder al feedback mediante IA Generativa: análisis profundo, en segundos, de forma gratuita.

</div>
</div>

---

<!-- _class: section-divider -->
<!-- _paginate: false -->
<!-- _footer: "" -->

# 🚀 Demo en vivo

**Flujo completo de la aplicación**

---

<!-- _footer: "Reto 9 — CV Assistant AI · Fundació URV · Mayo 2026" -->

# Demo — Flujo a mostrar

### Paso a paso

1. **Sidebar de configuración**
   - Sector: **Tecnología** · Puesto: **Senior Developer** · Experiencia: **5 años**

2. **Subir CV** → _test_cv_example.txt_

3. **Pulsar "Analizar CV"** → spinner de progreso

4. **Recorrer resultados**:
   - 📊 Puntuación general
   - 📋 Análisis por secciones
   - ✅ Fortalezas / ⚠️ Áreas de mejora
   - 💡 Sugerencias concretas
   - ✏️ Sección mejorada — original vs reescrita

5. **Descargar análisis** en formato JSON

---

<!-- _class: section-divider -->
<!-- _paginate: false -->
<!-- _footer: "" -->

# 🏗️ Arquitectura

**Stack tecnológico y decisiones de diseño**

---

<!-- _footer: "Reto 9 — CV Assistant AI · Fundació URV · Mayo 2026" -->

# Arquitectura de la Solución

### Stack tecnológico

| Capa       | Tecnología                                                                                                                                    | Rol                                         |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| Frontend   | <img src="https://cdn.simpleicons.org/streamlit/FF4B4B" height="18" style="vertical-align:middle"/> **Streamlit**                             | UI, upload, visualización, estado de sesión |
| LLM        | <img src="https://cdn.simpleicons.org/googlegemini/8E75B2" height="18" style="vertical-align:middle"/> **Gemini 3.1 Flash Lite** (OpenRouter) | Análisis del CV                             |
| Lenguaje   | <img src="https://cdn.simpleicons.org/python/3776AB" height="18" style="vertical-align:middle"/> **Python 3.11**                              | Backend completo                            |
| Extracción | **PyPDF2** + **python-docx**                                                                                                                  | Lectura PDF y DOCX                          |
| Prompting  | prompt_templates.py                                                                                                                           | 7 técnicas de prompt engineering            |
| Parseo     | 🔧 Parseo del json                                                                                                                            | JSON + 3 niveles de fallback                |
| Despliegue | <img src="https://cdn.simpleicons.org/github/181717" height="18" style="vertical-align:middle"/> **Streamlit Community Cloud**                | Hosting gratuito desde GitHub               |

---

<!-- _footer: "Reto 9 — CV Assistant AI · Fundació URV · Mayo 2026" -->

# Módulos del Proyecto

### Arquitectura modular en 5 componentes

| Módulo                 | Responsabilidad única                               |
| ---------------------- | --------------------------------------------------- |
| 🎛️ app.py              | Orquestador: UI, gestión de estado, pipeline        |
| 🤖 llm_integration.py  | conexión OpenRouter API, parámetros                 |
| 📝 prompt_templates.py | Prompt y analizador                                 |
| 🔧 parsers.py          | Extracción JSON, validación y fallback de 3 niveles |
| 📄 utils.py            | Extracción texto PDF / DOCX / TXT, limpieza         |

---

<!-- _footer: "Reto 9 — CV Assistant AI · Fundació URV · Mayo 2026" -->

# Decisiones Técnicas Clave

### ¿Por qué estas tecnologías y no otras?

| Decisión         | Elegido ✅                                                                                                                   | Descartado ❌                                                                                                       | Razón                                                  |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| **Framework UI** | <img src="https://cdn.simpleicons.org/streamlit/FF4B4B" height="16" style="vertical-align:middle"/> Streamlit                | FastAPI+React, Gradio                                                                                               | Python puro, componentes nativos, despliegue integrado |
| **Modelo LLM**   | <img src="https://cdn.simpleicons.org/googlegemini/8E75B2" height="16" style="vertical-align:middle"/> Gemini 3.1 Flash Lite | <img src="https://cdn.simpleicons.org/meta/0467DF" height="16" style="vertical-align:middle"/> Llama 3.1 70B (Groq) | Groq deprecated el modelo durante el desarrollo        |
| **API de LLM**   | 🔀 OpenRouter                                                                                                                | OpenAI direct                                                                                                       | Gratuito (500 req/día), compatible con SDK OpenAI      |
| **Despliegue**   | <img src="https://cdn.simpleicons.org/streamlit/FF4B4B" height="16" style="vertical-align:middle"/> Streamlit Cloud          | Heroku, AWS                                                                                                         | Gratuito, nativo Streamlit, secrets integrados         |
| **Parseo**       | 🔧 3 niveles fallback                                                                                                        | json.loads()simple                                                                                                  | El LLM se desvía ocasionalmente del formato            |

<br>

> **Decisión más impactante: `temperature = 0.2`**
> Reducir de 0.7 → 0.2 eliminó prácticamente todos los fallos de parseo JSON.
> Coherencia y determinismo por encima de creatividad en tareas estructuradas.

---

<!-- _class: section-divider -->
<!-- _paginate: false -->
<!-- _footer: "" -->

# 🧠 Prompt Engineering

**7 técnicas aplicadas y su impacto medido**

---

<!-- _footer: "Reto 9 — CV Assistant AI · Fundació URV · Mayo 2026" -->

# Prompt Engineering (1/2)

### Técnicas y su impacto

| Técnica                | Problema que resuelve                             | Impacto                                                     |
| ---------------------- | ------------------------------------------------- | ----------------------------------------------------------- |
| **Role Prompting**     | Vocabulario y criterios genéricos                 | Calibra tono, nivel de exigencia y vocabulario de RRHH      |
| **Context Setting**    | Evaluación descontextualizada                     | Relativiza la puntuación según sector, puesto y experiencia |
| **Chain-of-Thought**   | Output redundante y desorganizado                 | Coherencia entre los 8 campos del JSON                      |
| **Output Schema JSON** | Campos renombrados, decimales, estructura errónea | Fuerza contrato de datos estricto                           |

<br>

```text
SYSTEM: "Eres un experto senior en recursos humanos y revisión de CVs con más de 15 años de experiencia.
Siempre proporcionas respuestas ÚNICAMENTE en formato JSON válido, sin texto adicional."
```

---

<!-- _footer: "Reto 9 — CV Assistant AI · Fundació URV · Mayo 2026" -->

# Prompt Engineering (2/2)

### Técnicas y su impacto (continuación)

| Técnica                     | Problema que resuelve                                        | Impacto                                                         |
| --------------------------- | ------------------------------------------------------------ | --------------------------------------------------------------- |
| **Few-Shot Examples ×3**    | Modelo excesivamente benevolente (7–8/10 para CVs mediocres) | Calibra escala 0–10: bajo / medio / alto + 3 sectores distintos |
| **Instrucciones Negativas** | JSON envuelto en \`\`\`json, decimales, datos inventados     | Reduce fallos de parseo de ~30% a <5%                           |
| **Separación de datos**     | Prompt injection desde el CV                                 | CV al final, delimitado con `---`, post-instrucciones           |
| **Temperature = 0.2**       | Variabilidad en formato JSON                                 | Maximiza determinismo; elimina fallos de parseo residuales      |

<br>

````text
CRÍTICO: Devuelve ÚNICAMENTE el objeto JSON.
Cero texto antes ni después. No uses bloques ```json```.
Si el JSON no puede parsearse directamente, tu respuesta es inválida.
````

---

<!-- _footer: "Reto 9 — CV Assistant AI · Fundació URV · Mayo 2026" -->

# Sistema de Parseo — 3 Niveles de Fallback

### Requisito del reto: NO mostrar texto crudo al usuario

````
Respuesta del LLM
      ↓
Nivel 1: json.loads() directo          → ✅ ~90% de respuestas bien formadas
      ↓ fallo
Nivel 2: regex extrae bloque ```json```→ ✅ ~8% con markdown residual
      ↓ fallo
Nivel 3: regex extrae { ... }          → ✅ ~1.5% con texto prefijo/sufijo
      ↓ fallo
Fallback: get_fallback_analysis()      → análisis básico de error (~0.5%)
````

### Mapeo JSON → componentes Streamlit

| Campo del LLM          | Componente Streamlit                                  |
| ---------------------- | ----------------------------------------------------- |
| puntuacion_general     | st.metric                                             |
| analisis_secciones     | st.expander × 3 (experiencia, educación, habilidades) |
| fortalezas_principales | st.success (lista)                                    |
| areas_mejora`          | st.warning (lista)                                    |
| seccion_mejorada       | st.text_area comparativa (original vs mejorada)       |

---

<!-- _footer: "Reto 9 — CV Assistant AI · Fundació URV · Mayo 2026" -->

# Resultados y Validación

### Ejemplo de análisis real

**CV analizado**: Data Scientist · 3 años de experiencia · sector Tecnología

<div class="columns">
<div>

| Campo                    | Valor      |
| ------------------------ | ---------- |
| Puntuación general       | **6 / 10** |
| Puntuación Experiencia   | **7 / 10** |
| Puntuación Educación     | **8 / 10** |
| Puntuación Habilidades   | **4 / 10** |
| Nº sugerencias generadas | **6**      |

</div>
<div>

#### 🔑 Observación clave

Sin few-shot examples, el modelo puntuaba este mismo CV con **8/10** y generaba sugerencias genéricas del tipo _"mejora tu LinkedIn"_.

Con los 3 examples calibrados, la puntuación bajó a **6/10** y las sugerencias fueron 3× más concretas y accionables.

> Los examples calibran la escala. Sin ellos, el modelo es siempre benevolente.

</div>
</div>

---

<!-- _class: section-divider -->
<!-- _paginate: false -->
<!-- _footer: "" -->

# 💡 Conclusiones

**Lo que aprendimos**

---

<!-- _footer: "Reto 9 — CV Assistant AI · Fundació URV · Mayo 2026" -->

# Conclusiones

<div class="columns">
<div>

### ✅ Aprendizajes clave

**El prompt engineering importa más que el modelo**
La calidad del output depende más del diseño del prompt que del tamaño del modelo.

**Temperature baja = JSON consistente**
Reducir de 0.7 → 0.2 eliminó prácticamente todos los fallos de parseo.

**Few-shot examples calibran la escala**
Sin ejemplos, el modelo es sistemáticamente benevolente.

**El parseo robusto es obligatorio en producción**
El LLM se desvía del formato ocasionalmente; el fallback es imprescindible.

</div>
<div>

### 🔭 Trabajo futuro

- **Comparación CV vs ofertas reales**
  Integrar LinkedIn/Indeed API para contextualizar el análisis con requisitos de mercado

- **Soporte multilingüe**
  Análisis en inglés, francés y otros idiomas

- **OCR para CVs escaneados**
  Procesamiento de PDFs basados en imagen

- **Historial persistente entre sesiones**
  Base de datos para seguimiento de mejoras a lo largo del tiempo

</div>
</div>

---

<!-- _class: thanks -->
<!-- _paginate: false -->
<!-- _footer: "Javier Martín Castro · Reto 9 — IA Generativa · Artificial Intelligence Foundations · Fundació URV · Mayo 2026" -->

# ¡Gracias!

<br>

### 🔗 Links del proyecto

<img src="https://cdn.simpleicons.org/streamlit/FF4B4B" height="32" style="vertical-align:middle"/> <a href="https://cv-assistant-ai-ynjx6qsnd6prgwq3m4dipz.streamlit.app/">**App en producción**</a>

<img src="https://cdn.simpleicons.org/github/181717" height="32" style="vertical-align:middle"/> <a href="https://github.com/jamarcas1984/cv-assistant-ai">**Repositorio GitHub**</a>

<br>

---

<!-- _footer: "" -->
<!-- _paginate: false -->

<br><br>

![height:55](logoURVppd.png)

_Javier Martín Castro · Artificial Intelligence Foundations · Fundació Universitat Rovira i Virgili · Mayo 2026_
