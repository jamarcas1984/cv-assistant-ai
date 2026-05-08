# Plantilla para doc.pdf - Reto 9

## Estructura según Anexo I.2 (Aplicaciones integradas con GenAI)

---

### 1. Abstract (máx. 150 palabras)

[Escribir un resumen conciso que incluya]:

- Objetivo del proyecto
- Tecnologías principales utilizadas (Streamlit, Groq/Llama 3.1)
- Funcionalidad principal (análisis automatizado de CVs)
- Resultados/logros principales
- Técnicas de prompt engineering aplicadas

**Ejemplo:**

> Este proyecto implementa un asistente inteligente para la revisión y mejora de currículums vitae utilizando IA Generativa. La aplicación, desarrollada con Streamlit, integra el modelo Llama 3.1 70B a través de la API de Groq para proporcionar análisis detallados, identificación de fortalezas/debilidades y sugerencias concretas de mejora. Se aplican técnicas avanzadas de prompt engineering incluyendo role prompting, output formatting estructurado en JSON, y chain-of-thought reasoning. El sistema parsea y mapea automáticamente las respuestas del LLM a componentes visuales de Streamlit, cumpliendo con los requisitos de no mostrar texto crudo. Los resultados demuestran la efectividad de la IA generativa para automatizar procesos de revisión profesional que tradicionalmente requerían intervención humana experta.

---

### 2. Introducción

#### 2.1 Contexto del Problema

[Describir]:

- Importancia de un buen CV en el mercado laboral
- Dificultades comunes al elaborar un CV
- Necesidad de feedback profesional
- Cómo la IA puede ayudar en este proceso

#### 2.2 Objetivos del Proyecto

- Objetivo principal
- Objetivos específicos (análisis, sugerencias, mejoras, etc.)

#### 2.3 Alcance

- Qué incluye el proyecto
- Qué no incluye (limitaciones conocidas)

---

### 3. Implementación de la Aplicación

#### 3.1 Arquitectura General

```
Usuario → Streamlit UI → CVAnalyzer → Groq API (Llama 3.1) → Parsers → Visualización
```

[Incluir diagrama de flujo o arquitectura]

#### 3.2 Descripción Detallada de las Vistas

##### Vista Principal

- Título y descripción
- Área de carga de archivos
- Botón de análisis

##### Sidebar de Configuración

- Selector de sector profesional
- Campo de puesto objetivo
- Slider de años de experiencia

##### Vista de Resultados

- Métricas de puntuación general
- Tarjetas de análisis por secciones
- Listas de fortalezas y debilidades
- Sugerencias de mejora
- Ejemplo de sección mejorada

#### 3.3 Funcionalidades Ofrecidas

1. **Upload de CV**: Soporte para PDF, DOCX y TXT
2. **Extracción de texto**: Procesamiento automático según formato
3. **Análisis contextual**: Considerando sector, puesto y experiencia
4. **Visualización estructurada**: Componentes Streamlit para cada sección
5. **Descarga de resultados**: Exportación en formato JSON

---

### 4. Integración con LLM

#### 4.1 Selección del Modelo

**Modelo elegido**: Llama 3.1 70B Versatile (via Groq API)

**Justificación**:

1. **Capacidad de análisis**: 70B parámetros proporcionan comprensión profunda
2. **Seguimiento de instrucciones**: Excelente para prompts estructurados
3. **Velocidad**: Groq ofrece inferencia ultra-rápida
4. **Coste**: API gratuita con límites generosos para desarrollo
5. **Calidad de output**: Balance óptimo entre precisión y creatividad

**Alternativas consideradas**:

- GPT-3.5: Rechazado por coste de API
- Mixtral 8x7B: Considerado pero Llama 3.1 mostró mejores resultados
- Claude: No disponible en APIs gratuitas

#### 4.2 Flujo de Comunicación App/LLM

```
1. Usuario sube CV → 2. Extracción de texto →
3. Limpieza y normalización → 4. Creación de prompt →
5. Llamada a Groq API → 6. Respuesta del LLM →
7. Parseo de JSON → 8. Validación →
9. Mapeo
```
