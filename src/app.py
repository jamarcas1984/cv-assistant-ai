"""
Aplicación Streamlit para análisis de CVs con IA.
"""

import streamlit as st

from llm_integration import CVAnalyzer
from parsers import get_fallback_analysis, parse_cv_analysis, validate_cv_analysis
from utils import clean_cv_text, extract_text_from_file

# Configuración de la página
st.set_page_config(
    page_title="CV Assistant AI",
    page_icon="💭",
    layout="wide",
    initial_sidebar_state="expanded",
)


def init_session_state():
    """Inicializa el estado de la sesión."""
    if "analyzer" not in st.session_state:
        try:
            st.session_state.analyzer = CVAnalyzer()
        except ValueError as e:
            st.error(f"❌ Error de configuración: {str(e)}")
            st.info(
                "💡 **Solución**: Crea un archivo `.env` con tu OPENROUTER_API_KEY. "
                "Obtén tu API key en https://openrouter.ai/keys"
            )
            st.stop()

    if "analysis_result" not in st.session_state:
        st.session_state.analysis_result = None

    # Historial de llamadas al LLM para el panel de costes
    if "usage_history" not in st.session_state:
        st.session_state.usage_history = []


def get_rating_label(puntuacion: int) -> str:
    """Retorna etiqueta según puntuación."""
    if puntuacion >= 8:
        return "Excelente"
    elif puntuacion >= 7:
        return "Muy Bueno"
    elif puntuacion >= 5:
        return "Aceptable"
    elif puntuacion >= 3:
        return "Necesita Mejora"
    else:
        return "Insuficiente"


def render_sidebar():
    """Renderiza la barra lateral con configuración."""
    with st.sidebar:
        st.header("⚙️ Configuración")
        st.markdown("---")

        sector = st.selectbox(
            "🏢 Sector profesional",
            [
                "Tecnología",
                "Marketing",
                "Finanzas",
                "Salud",
                "Educación",
                "Ventas",
                "Recursos Humanos",
                "Ingeniería",
                "Diseño",
                "Otro",
            ],
        )

        puesto = st.text_input(
            "💼 Puesto objetivo", placeholder="Ej: Desarrollador Senior..."
        )

        experiencia = st.slider("📅 Años de experiencia", 0, 30, 5)

        st.markdown("---")
        st.markdown("### 📚 Sobre este proyecto")
        st.caption(
            """
        **Reto 9**: Asistente de revisión y mejora de CVs
        
        **Técnicas de Prompt Engineering**:
        - Role Prompting
        - Output Formatting
        - Chain-of-Thought
        - Temperature Control
        """
        )

    return sector, puesto, experiencia


def render_analysis_results(analysis):
    """Renderiza los resultados del análisis."""
    st.markdown("## 📊 Puntuación General")

    col1, col2, col3 = st.columns(3)

    with col1:
        puntuacion = analysis.get("puntuacion_general", 0)
        color = "🟢" if puntuacion >= 7 else "🟡" if puntuacion >= 5 else "🔴"
        st.metric(
            "Puntuación del CV",
            f"{puntuacion}/10",
            delta=f"{color} {get_rating_label(puntuacion)}",
        )

    with col2:
        secciones = analysis.get("analisis_secciones", {})
        if secciones:
            promedio = sum(s.get("puntuacion", 0) for s in secciones.values()) / len(
                secciones
            )
            st.metric("Promedio Secciones", f"{promedio:.1f}/10")

    with col3:
        mejoras = len(analysis.get("mejoras_sugeridas", []))
        st.metric("Sugerencias", mejoras)

    if analysis.get("resumen_general"):
        st.info(f"**Resumen**: {analysis['resumen_general']}")

    # Análisis por secciones
    st.markdown("## 📋 Análisis por Secciones")

    secciones = analysis.get("analisis_secciones", {})
    if secciones:
        for nombre, datos in secciones.items():
            with st.expander(f"📌 {nombre.title()}", expanded=True):
                col1, col2 = st.columns([1, 3])

                with col1:
                    st.metric("Puntuación", f"{datos.get('puntuacion', 0)}/10")

                with col2:
                    if datos.get("fortalezas"):
                        st.markdown("**✅ Fortalezas:**")
                        for f in datos["fortalezas"]:
                            st.markdown(f"- {f}")

                    if datos.get("debilidades"):
                        st.markdown("**⚠️ Áreas de mejora:**")
                        for d in datos["debilidades"]:
                            st.markdown(f"- {d}")

                if datos.get("sugerencias"):
                    st.markdown(f"**💡 Sugerencias:** {datos['sugerencias']}")

    # Fortalezas y debilidades generales
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("## ✅ Fortalezas Principales")
        for fortaleza in analysis.get("fortalezas_principales", []):
            st.success(f"✓ {fortaleza}")

    with col2:
        st.markdown("## ⚠️ Áreas de Mejora")
        for area in analysis.get("areas_mejora", []):
            st.warning(f"⚡ {area}")

    # Mejoras sugeridas
    st.markdown("## 💡 Mejoras Sugeridas")
    for i, mejora in enumerate(analysis.get("mejoras_sugeridas", []), 1):
        st.info(f"**{i}.** {mejora}")

    # Sección mejorada
    if analysis.get("seccion_mejorada"):
        st.markdown("## 🎯 Ejemplo de Mejora")
        seccion_mejorada = analysis["seccion_mejorada"]

        st.markdown(f"### {seccion_mejorada.get('nombre_seccion', 'N/A')}")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**📄 Versión Original:**")
            st.text_area(
                "Original",
                seccion_mejorada.get("version_original", "N/A"),
                height=200,
                key="original",
                label_visibility="collapsed",
            )

        with col2:
            st.markdown("**✨ Versión Mejorada:**")
            st.text_area(
                "Mejorada",
                seccion_mejorada.get("version_mejorada", "N/A"),
                height=200,
                key="mejorada",
                label_visibility="collapsed",
            )


def render_usage_dashboard():
    """Renderiza el panel de uso de tokens y costes estimados."""
    history = st.session_state.usage_history
    if not history:
        st.info("ℹ️ Aún no se han realizado análisis en esta sesión.")
        return

    st.markdown("## 💰 Uso de Tokens y Costes Estimados")
    st.caption(
        "Precios de referencia: Gemini 3.1 Flash Lite vía OpenRouter — "
        "Input: $0.10/M tokens · Output: $0.40/M tokens"
    )

    # ── Métricas resumen ────────────────────────────────────────────────────
    total_prompt = sum(r["prompt_tokens"] for r in history)
    total_completion = sum(r["completion_tokens"] for r in history)
    total_tokens = sum(r["total_tokens"] for r in history)
    total_cost = sum(r["cost_usd"] for r in history)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("🔢 Análisis realizados", len(history))
    col2.metric("📥 Tokens entrada (total)", f"{total_prompt:,}")
    col3.metric("📤 Tokens salida (total)", f"{total_completion:,}")
    col4.metric("💵 Coste acumulado (USD)", f"${total_cost:.6f}")

    st.markdown("---")

    # ── Gráfica de tokens por llamada ───────────────────────────────────────
    labels = [f"#{i + 1} {r['archivo']}" for i, r in enumerate(history)]

    col_left, col_right = st.columns(2)

    with col_left:
        st.markdown("### 📊 Tokens por análisis")
        token_data = {
            "Entrada (prompt)": [r["prompt_tokens"] for r in history],
            "Salida (completion)": [r["completion_tokens"] for r in history],
        }
        st.bar_chart(token_data, x_label="Análisis", y_label="Tokens")

    with col_right:
        st.markdown("### 💵 Coste estimado por análisis (USD)")
        cost_data = {"Coste USD": [r["cost_usd"] for r in history]}
        st.bar_chart(cost_data, x_label="Análisis", y_label="USD")

    # ── Tabla detalle ────────────────────────────────────────────────────────
    st.markdown("### 📋 Detalle por llamada")
    table_rows = []
    for i, r in enumerate(history):
        table_rows.append(
            {
                "Análisis": f"#{i + 1}",
                "Archivo": r["archivo"],
                "Tokens entrada": r["prompt_tokens"],
                "Tokens salida": r["completion_tokens"],
                "Total tokens": r["total_tokens"],
                "Coste (USD)": f"${r['cost_usd']:.6f}",
            }
        )
    st.dataframe(table_rows, use_container_width=True)


def main():
    """Función principal de la aplicación."""
    init_session_state()

    # Título
    st.markdown("# 🎯 CV Assistant AI")
    st.markdown(
        "### Asistente inteligente para revisión y mejora de currículums vitae"
    )
    st.markdown("---")

    # Sidebar
    sector, puesto, experiencia = render_sidebar()

    # Pestañas principales
    tab_analisis, tab_costes = st.tabs(["🔍 Análisis de CV", "📈 Uso y Costes"])

    with tab_analisis:
        # Upload de archivo
        st.markdown("## 📃 Sube tu CV")

        uploaded_file = st.file_uploader(
            "Selecciona tu CV (PDF, DOCX o TXT)",
            type=["pdf", "docx", "txt"],
            help="Formatos soportados: PDF, DOCX, TXT. Tamaño máximo: 10MB",
        )

        if uploaded_file:
            st.success(f"✓ Archivo cargado: {uploaded_file.name}")

            # Validar campos requeridos
            if not puesto:
                st.warning(
                    "⚠️ Por favor, especifica el puesto objetivo en la barra lateral"
                )
            else:
                # Botón de análisis
                if st.button("🚀 Analizar CV", type="primary"):
                    with st.spinner(
                        "🔄 Analizando tu CV... Esto puede tomar unos segundos."
                    ):
                        try:
                            # Extraer texto del archivo
                            file_bytes = uploaded_file.read()
                            file_type = uploaded_file.name.split(".")[-1].lower()

                            cv_text = extract_text_from_file(file_bytes, file_type)
                            cv_text = clean_cv_text(cv_text)

                            if not cv_text or len(cv_text) < 100:
                                st.error(
                                    "❌ El archivo parece estar vacío o no se pudo "
                                    "extraer el texto correctamente."
                                )
                            else:
                                # Analizar con LLM — devuelve dict con content + usage
                                llm_result = st.session_state.analyzer.analyze_cv(
                                    cv_text, sector, puesto, experiencia
                                )

                                llm_output = llm_result["content"]

                                # Registrar uso en el historial
                                st.session_state.usage_history.append(
                                    {
                                        "archivo": uploaded_file.name,
                                        "prompt_tokens": llm_result["prompt_tokens"],
                                        "completion_tokens": llm_result[
                                            "completion_tokens"
                                        ],
                                        "total_tokens": llm_result["total_tokens"],
                                        "cost_usd": llm_result["cost_usd"],
                                    }
                                )

                                # Parsear respuesta
                                analysis = parse_cv_analysis(llm_output)

                                if analysis and validate_cv_analysis(analysis):
                                    st.session_state.analysis_result = analysis
                                    st.success("✅ Análisis completado exitosamente!")
                                    tokens_info = (
                                        f"🔢 Tokens usados: "
                                        f"{llm_result['total_tokens']:,} "
                                        f"(entrada: {llm_result['prompt_tokens']:,} · "
                                        f"salida: {llm_result['completion_tokens']:,}) — "
                                        f"Coste estimado: ${llm_result['cost_usd']:.6f}"
                                    )
                                    st.caption(tokens_info)
                                else:
                                    st.warning(
                                        "⚠️ No se pudo parsear la respuesta correctamente. "
                                        "Mostrando análisis básico."
                                    )
                                    st.session_state.analysis_result = (
                                        get_fallback_analysis()
                                    )
                                    with st.expander("🔍 Ver respuesta del LLM (debug)"):
                                        st.code(llm_output)

                        except Exception as e:
                            st.error(f"❌ Error al analizar el CV: {str(e)}")
                            st.session_state.analysis_result = None

        # Mostrar resultados si existen
        if st.session_state.analysis_result:
            st.markdown("---")
            render_analysis_results(st.session_state.analysis_result)

            # Botón para descargar análisis
            st.markdown("---")
            st.download_button(
                label="📥 Descargar análisis (JSON)",
                data=str(st.session_state.analysis_result),
                file_name="analisis_cv.json",
                mime="application/json",
            )

    with tab_costes:
        render_usage_dashboard()


if __name__ == "__main__":
    main()
