"""
Templates de prompts para el análisis de CVs.
Incluye técnicas de prompt engineering para maximizar la calidad del output.
"""

# Role prompting: rol específico, dominio explícito, tarea única y restricción de output
SYSTEM_PROMPT = """Eres un experto senior en recursos humanos y revisión de CVs con más de 15 años de experiencia.
Tu especialidad es analizar CVs y proporcionar feedback estructurado, concreto y accionable.
Siempre proporcionas respuestas ÚNICAMENTE en formato JSON válido, sin texto adicional antes ni después."""


def create_cv_analysis_prompt(
    cv_text: str, sector: str, puesto: str, experiencia: int
) -> str:
    """
    Crea un prompt estructurado para el análisis de CV.

    Técnicas de prompt engineering aplicadas:
    1. Role prompting: Definición del rol experto en RRHH (en SYSTEM_PROMPT)
    2. Context setting: Contexto del candidato antes de las instrucciones
    3. Chain-of-thought: Razonamiento guiado mediante pasos numerados
    4. Output schema: Estructura JSON explícita con todos los campos y rangos de valores
    5. Few-shot examples: Ejemplos representativos de análisis reales del dominio
    6. Instrucciones negativas: Restricciones explícitas para evitar alucinaciones
    7. Separación de datos: El texto del CV va delimitado y al final, tras las instrucciones

    Args:
        cv_text: Texto completo del CV a analizar
        sector: Sector profesional objetivo
        puesto: Puesto al que aspira el candidato
        experiencia: Años de experiencia del candidato

    Returns:
        Prompt estructurado para el LLM
    """
    prompt = f"""## CONTEXTO DEL CANDIDATO

- Sector objetivo: {sector}
- Puesto objetivo: {puesto}
- Años de experiencia declarados: {experiencia}

## INSTRUCCIONES DE ANÁLISIS

Analiza el CV del candidato siguiendo estos pasos en orden:

1. **Evaluación General** (puntuación entera de 0 a 10):
   - Evalúa estructura, claridad, formato y relevancia global del CV
   - Considera el ajuste entre el CV y el sector/puesto objetivo indicados

2. **Análisis por Secciones** (Experiencia, Educación, Habilidades):
   - Para cada sección: identifica fortalezas, áreas de mejora y asigna puntuación entera 0-10
   - Si una sección no existe en el CV, puntúa 0 e indícalo en debilidades

3. **Fortalezas y Áreas de Mejora Globales**:
   - Lista entre 3 y 5 fortalezas principales del CV en su conjunto
   - Lista entre 3 y 5 áreas de mejora del CV en su conjunto

4. **Sugerencias Concretas**:
   - Proporciona entre 5 y 7 mejoras específicas, accionables e implementables de forma inmediata

5. **Ejemplo de Mejora**:
   - Selecciona la sección con puntuación más baja
   - Reescribe esa sección aplicando todas las mejoras sugeridas

## INSTRUCCIONES NEGATIVAS

CRÍTICO — Formato de respuesta:
- Devuelve ÚNICAMENTE el objeto JSON. Cero texto antes ni después del JSON.
- No uses bloques markdown (```json), no añadas explicaciones, no incluyas comentarios.
- Si el JSON no puede ser parseado directamente, tu respuesta es inválida.

CRÍTICO — Valores numéricos:
- Todos los campos "puntuacion" deben ser enteros entre 0 y 10, nunca null, nunca decimales.
- No uses porcentajes ni escalas distintas a 0-10.

CRÍTICO — Datos del CV:
- Usa SOLO la información que aparece en el CV. No inventes experiencias, títulos ni habilidades.
- Si una sección no aparece en el CV (p.ej. no hay sección de educación), puntuación = 0 y
  indica "Sección no encontrada en el CV" en debilidades.

## FEW-SHOT EXAMPLES

Ejemplo 1 — CV básico de recién graduado (sector Tecnología, puesto Junior Developer):
Output esperado:
{{"puntuacion_general": 4, "resumen_general": "CV de recién graduado con buena formación técnica pero sin experiencia laboral demostrada. Estructura clara pero le falta impacto y logros cuantificables.", "analisis_secciones": {{"experiencia": {{"puntuacion": 2, "fortalezas": ["Incluye prácticas en empresa"], "debilidades": ["Sin experiencia laboral real", "No cuantifica logros"], "sugerencias": "Añade proyectos personales o de universidad con resultados medibles. Indica tecnologías concretas usadas."}}, "educacion": {{"puntuacion": 7, "fortalezas": ["Grado relevante", "Nota media alta"], "debilidades": ["No menciona proyectos fin de grado"], "sugerencias": "Incluye el TFG con una línea describiendo el problema resuelto y la tecnología empleada."}}, "habilidades": {{"puntuacion": 5, "fortalezas": ["Lista de tecnologías relevante"], "debilidades": ["No diferencia nivel de dominio", "Mezcla soft y hard skills"], "sugerencias": "Separa habilidades técnicas de competencias personales. Indica nivel (básico/intermedio/avanzado)."}}}}, "fortalezas_principales": ["Formación académica sólida y reciente", "Conocimiento de tecnologías actuales", "Perfil ordenado y legible"], "areas_mejora": ["Ausencia de experiencia laboral demostrable", "Sin logros cuantificables", "Falta de proyectos propios"], "mejoras_sugeridas": ["Añadir sección de proyectos personales con GitHub", "Cuantificar cualquier logro (notas, participantes, resultados)", "Incluir certificaciones online (AWS, Google, etc.)", "Añadir LinkedIn y GitHub al encabezado", "Reescribir el perfil profesional orientándolo al puesto objetivo"], "seccion_mejorada": {{"nombre_seccion": "Experiencia", "version_original": "Prácticas en empresa XYZ, 2023", "version_mejorada": "Desarrollador en prácticas — XYZ Solutions (Feb–Jun 2023)\\n• Desarrollé 3 microservicios REST con Python/FastAPI reduciendo el tiempo de respuesta en un 20%\\n• Colaboré en equipo ágil de 5 personas usando Git y metodología Scrum\\n• Integré tests unitarios con pytest, alcanzando 85% de cobertura"}}}}

Ejemplo 2 — CV de profesional de nivel medio (sector Marketing, puesto Marketing Manager con 5 años de experiencia):
Output esperado:
{{"puntuacion_general": 5, "resumen_general": "CV con experiencia relevante y formación adecuada, pero con carencias importantes: los logros no están cuantificados, la sección de habilidades es genérica y el perfil de cabecera no diferencia al candidato. Necesita revisión sustancial para ser competitivo.", "analisis_secciones": {{"experiencia": {{"puntuacion": 6, "fortalezas": ["3 años en empresa del sector", "Variedad de campañas gestionadas"], "debilidades": ["Logros descritos sin métricas (sin ROI, sin conversiones, sin presupuesto gestionado)", "Responsabilidades copiadas de descripciones de puesto genéricas"], "sugerencias": "Transforma cada responsabilidad en un logro: en lugar de 'gestión de redes sociales', escribe 'Crecimiento de comunidad en Instagram de 2K a 18K seguidores en 12 meses (+800%). CTR medio del 4,2%'."}}, "educacion": {{"puntuacion": 7, "fortalezas": ["Grado en ADE con mención en Marketing", "Curso de Google Analytics certificado"], "debilidades": ["No menciona TFG ni proyectos académicos relevantes"], "sugerencias": "Añade una línea sobre el TFG si es relevante para el puesto. Incluye la fecha de obtención del certificado de Google Analytics para demostrar que está vigente."}}, "habilidades": {{"puntuacion": 4, "fortalezas": ["Menciona herramientas de marketing digital"], "debilidades": ["Lista plana sin nivel de dominio", "Incluye soft skills genéricas (trabajo en equipo, proactividad) sin respaldo", "No menciona CRM ni herramientas de automatización"], "sugerencias": "Organiza por categorías: Herramientas (Google Ads, Meta Ads, HubSpot), Analítica (GA4, Looker Studio), Idiomas. Elimina soft skills sin evidencia y sustitúyelas por competencias con resultados."}}}}, "fortalezas_principales": ["Experiencia en el sector relevante para el puesto", "Formación académica adecuada", "Conocimiento de herramientas de marketing digital"], "areas_mejora": ["Logros sin cuantificar en toda la experiencia laboral", "Habilidades genéricas sin nivel ni evidencia", "Perfil de cabecera que no diferencia al candidato", "Ausencia de métricas de impacto"], "mejoras_sugeridas": ["Cuantificar cada logro: añadir porcentajes, cifras de presupuesto o resultados de campaña", "Reescribir el perfil profesional destacando 2-3 logros clave y el valor diferencial", "Añadir herramientas de CRM (HubSpot, Salesforce) y automatización (Mailchimp, ActiveCampaign)", "Incluir enlace a portfolio de campañas o perfil de LinkedIn", "Eliminar soft skills genéricas y sustituirlas por competencias con evidencia", "Añadir métricas de las campañas más relevantes (ROAS, CPL, tasa de apertura de email)"], "seccion_mejorada": {{"nombre_seccion": "Habilidades", "version_original": "Google Ads, Facebook Ads, Photoshop, Excel, trabajo en equipo, proactividad, inglés", "version_mejorada": "Marketing digital: Google Ads (certificado Google, campaña máx. 50K€/mes), Meta Ads, SEO/SEM\\nAnalítica: Google Analytics 4, Looker Studio, Excel avanzado (tablas dinámicas, VLOOKUP)\\nAutomatización y CRM: HubSpot (Marketing Hub), Mailchimp\\nCreación de contenido: Canva, Adobe Photoshop (nivel medio)\\nIdiomas: Español (nativo), Inglés (B2 — First Certificate 2021)"}}}}

Ejemplo 3 — CV de profesional senior bien estructurado (sector Finanzas, puesto CFO):
Output esperado:
{{"puntuacion_general": 8, "resumen_general": "CV sólido de profesional con larga trayectoria en finanzas. Logros bien cuantificados y progresión de carrera clara. Podría mejorar la sección de habilidades digitales y el perfil de cabecera.", "analisis_secciones": {{"experiencia": {{"puntuacion": 9, "fortalezas": ["Progresión clara de carrera", "Logros cuantificados con €", "Empresas reconocidas"], "debilidades": ["Último puesto sin fecha de fin"], "sugerencias": "Completa la fecha del puesto actual con 'Actualidad'. Añade una línea de impacto para cada posición."}}, "educacion": {{"puntuacion": 8, "fortalezas": ["MBA en escuela de prestigio", "Formación continua demostrada"], "debilidades": ["Formaciones antiguas sin relevancia actual"], "sugerencias": "Elimina cursos de hace más de 10 años sin relevancia. Destaca certificaciones vigentes como CFA o ACCA."}}, "habilidades": {{"puntuacion": 5, "fortalezas": ["Dominio de herramientas financieras"], "debilidades": ["Sin mención a herramientas de BI ni analítica de datos", "Idiomas sin nivel acreditado"], "sugerencias": "Añade Power BI, Tableau o Excel avanzado. Indica nivel de idiomas con certificación (C1, B2, etc.)."}}}}, "fortalezas_principales": ["Experiencia directiva contrastada", "Logros económicos cuantificados", "Formación de alto nivel", "Progresión profesional coherente"], "areas_mejora": ["Habilidades digitales poco desarrolladas", "Idiomas sin acreditación", "Perfil de cabecera genérico"], "mejoras_sugeridas": ["Reescribir el perfil profesional con 3 logros clave en 3 líneas", "Añadir herramientas de analítica financiera (Power BI, SAP)", "Acreditar nivel de idiomas con certificación oficial", "Incluir métricas de impacto en cada posición directiva", "Añadir sección de consejos/comités si aplica"], "seccion_mejorada": {{"nombre_seccion": "Habilidades", "version_original": "Excel, Word, inglés, francés, trabajo en equipo, liderazgo", "version_mejorada": "Herramientas financieras: SAP FI/CO (avanzado), Oracle Financials, Power BI, Excel (tablas dinámicas, macros VBA)\\nIdiomas: Español (nativo), Inglés (C1 — Cambridge CAE 2019), Francés (B2)\\nCompetencias directivas: Liderazgo de equipos (+50 personas), gestión del cambio, negociación con inversores"}}}}

## CV A ANALIZAR

---
{cv_text}
---

## SCHEMA DE SALIDA JSON

Devuelve ÚNICAMENTE el siguiente JSON con los valores reales del análisis. Sin texto adicional.

{{
  "puntuacion_general": entero entre 0 y 10,
  "resumen_general": "string — resumen ejecutivo del CV en 2-3 frases",
  "analisis_secciones": {{
    "experiencia": {{
      "puntuacion": entero entre 0 y 10,
      "fortalezas": ["string", "string"],
      "debilidades": ["string", "string"],
      "sugerencias": "string — mejoras específicas para esta sección"
    }},
    "educacion": {{
      "puntuacion": entero entre 0 y 10,
      "fortalezas": ["string"],
      "debilidades": ["string"],
      "sugerencias": "string"
    }},
    "habilidades": {{
      "puntuacion": entero entre 0 y 10,
      "fortalezas": ["string"],
      "debilidades": ["string"],
      "sugerencias": "string"
    }}
  }},
  "fortalezas_principales": ["string", "string", "string"],
  "areas_mejora": ["string", "string", "string"],
  "mejoras_sugeridas": [
    "string — mejora concreta y accionable 1",
    "string — mejora concreta y accionable 2",
    "string — mejora concreta y accionable 3",
    "string — mejora concreta y accionable 4",
    "string — mejora concreta y accionable 5"
  ],
  "seccion_mejorada": {{
    "nombre_seccion": "string — nombre de la sección con menor puntuación",
    "version_original": "string — texto original extraído del CV",
    "version_mejorada": "string — versión reescrita con todas las mejoras aplicadas"
  }}
}}
"""
    return prompt