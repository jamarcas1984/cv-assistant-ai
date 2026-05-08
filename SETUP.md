# 🚀 Guía de Configuración - CV Assistant AI

## Pasos para poner en marcha el proyecto

### 1. Crear entorno virtual

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/macOS
python -m venv .venv
source .venv/bin/activate
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Configurar API key de Groq

#### 3.1 Obtener API key

1. Visita [https://console.groq.com](https://console.groq.com)
2. Crea una cuenta gratuita
3. Ve a "API Keys"
4. Genera una nueva API key

#### 3.2 Configurar archivo .env

```bash
# Copiar el archivo de ejemplo
cp .env.example .env

# Editar .env con tu editor preferido
# Pegar tu API key en OPENROUTER_API_KEY
```

Tu archivo `.env` debe verse así:

```
OPENROUTER_API_KEY=gsk_tu_api_key_aqui
MODEL_NAME=llama-3.1-70b-versatile
```

### 4. Ejecutar la aplicación

```bash
streamlit run src/app.py
```

La aplicación se abrirá automáticamente en `http://localhost:8501`

## 🧪 Probar la aplicación

1. **Configurar parámetros** en el sidebar:
   - Sector profesional
   - Puesto objetivo
   - Años de experiencia

2. **Subir un CV**:
   - Formatos: PDF, DOCX o TXT
   - Puedes usar CVs de ejemplo para pruebas

3. **Analizar**:
   - Click en "🚀 Analizar CV"
   - Espera unos segundos mientras la IA procesa

4. **Revisar resultados**:
   - Puntuación general
   - Análisis por secciones
   - Sugerencias de mejora

## 🔧 Solución de problemas

### Error: OPENROUTER_API_KEY no encontrada

**Problema**: No se configuró correctamente el archivo `.env`

**Solución**:

1. Verifica que existe el archivo `.env` en la raíz del proyecto
2. Verifica que la API key está correctamente copiada
3. Reinicia la aplicación Streamlit

### Error al extraer texto del PDF

**Problema**: El PDF puede estar protegido o corrupto

**Solución**:

1. Intenta con otro formato (TXT o DOCX)
2. Verifica que el PDF no esté protegido con contraseña
3. Prueba con un PDF diferente

### Error de conexión a Groq API

**Problema**: Problemas de red o límite de rate limit

**Solución**:

1. Verifica tu conexión a internet
2. Espera unos minutos si alcanzaste el rate limit
3. Verifica que tu API key sea válida

## 📚 Próximos pasos

Una vez que la aplicación funcione localmente:

1. ✅ **Probar con diferentes CVs**
2. ✅ **Ajustar prompts** si es necesario
3. ✅ **Preparar documentación** (doc.pdf)
4. ✅ **Crear presentación** (slides.pdf)
5. ✅ **Grabar vídeo demo** (3 min max)
6. ✅ **Desplegar en Streamlit Cloud**
7. ✅ **Subir a GitHub** (repositorio público)

## 🌐 Despliegue en Streamlit Cloud

### Paso 1: Preparar repositorio

```bash
git init
git add .
git commit -m "Initial commit: CV Assistant AI"
git remote add origin https://github.com/tu-usuario/tu-repo.git
git push -u origin main
```

### Paso 2: Configurar Streamlit Cloud

1. Ve a [https://streamlit.io/cloud](https://streamlit.io/cloud)
2. Conecta con tu cuenta de GitHub
3. Selecciona tu repositorio
4. Configura:
   - Main file path: `src/app.py`
   - Python version: 3.12

### Paso 3: Configurar Secrets

En la configuración de la app en Streamlit Cloud, añade:

```toml
OPENROUTER_API_KEY = "tu_api_key_aqui"
MODEL_NAME = "llama-3.1-70b-versatile"
```

### Paso 4: Deploy

Click en "Deploy" y espera unos minutos.

¡Tu aplicación estará disponible en una URL pública!

## 📝 Notas adicionales

- **Límites de Groq**: La API gratuita tiene límites de requests. Úsala con moderación.
- **Tamaño de CVs**: Recomendado < 5 páginas para mejores resultados
- **Idioma**: El sistema funciona mejor con CVs en español o inglés

## 🆘 Soporte

Si encuentras problemas, revisa:

1. [Documentación de Streamlit](https://docs.streamlit.io)
2. [Documentación de Groq](https://console.groq.com/docs)
3. Contacta al profesor del curso para dudas específicas del reto

---

**¡Buena suerte con tu proyecto!** 🎯
