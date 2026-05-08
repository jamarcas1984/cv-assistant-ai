"""
Utilidades para procesamiento de archivos y funciones auxiliares.
"""

import io
from typing import Optional

import docx
import PyPDF2


def extract_text_from_pdf(file_bytes: bytes) -> str:
    """
    Extrae texto de un archivo PDF.

    Args:
        file_bytes: Bytes del archivo PDF

    Returns:
        Texto extraído del PDF

    Raises:
        Exception: Si hay error al procesar el PDF
    """
    try:
        pdf_file = io.BytesIO(file_bytes)
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        text_parts = []
        for page in pdf_reader.pages:
            text_parts.append(page.extract_text())

        return "\n\n".join(text_parts)
    except Exception as e:
        raise Exception(f"Error al extraer texto del PDF: {str(e)}")


def extract_text_from_docx(file_bytes: bytes) -> str:
    """
    Extrae texto de un archivo DOCX.

    Args:
        file_bytes: Bytes del archivo DOCX

    Returns:
        Texto extraído del DOCX

    Raises:
        Exception: Si hay error al procesar el DOCX
    """
    try:
        docx_file = io.BytesIO(file_bytes)
        doc = docx.Document(docx_file)

        text_parts = []
        for paragraph in doc.paragraphs:
            if paragraph.text.strip():
                text_parts.append(paragraph.text)

        return "\n\n".join(text_parts)
    except Exception as e:
        raise Exception(f"Error al extraer texto del DOCX: {str(e)}")


def extract_text_from_txt(file_bytes: bytes) -> str:
    """
    Extrae texto de un archivo TXT.

    Args:
        file_bytes: Bytes del archivo TXT

    Returns:
        Texto extraído del TXT

    Raises:
        Exception: Si hay error al procesar el TXT
    """
    try:
        return file_bytes.decode("utf-8")
    except UnicodeDecodeError:
        try:
            return file_bytes.decode("latin-1")
        except Exception as e:
            raise Exception(f"Error al decodificar el archivo de texto: {str(e)}")


def extract_text_from_file(file_bytes: bytes, file_type: str) -> Optional[str]:
    """
    Extrae texto de un archivo según su tipo.

    Args:
        file_bytes: Bytes del archivo
        file_type: Tipo de archivo ('pdf', 'docx', 'txt')

    Returns:
        Texto extraído del archivo o None si hay error

    Raises:
        ValueError: Si el tipo de archivo no es soportado
    """
    file_type = file_type.lower()

    if file_type == "pdf":
        return extract_text_from_pdf(file_bytes)
    elif file_type in ["docx", "doc"]:
        return extract_text_from_docx(file_bytes)
    elif file_type == "txt":
        return extract_text_from_txt(file_bytes)
    else:
        raise ValueError(f"Tipo de archivo no soportado: {file_type}")


def clean_cv_text(text: str) -> str:
    """
    Limpia y normaliza el texto extraído de un CV.

    Args:
        text: Texto crudo del CV

    Returns:
        Texto limpio y normalizado
    """
    # Eliminar espacios en blanco excesivos
    lines = [line.strip() for line in text.split("\n")]
    lines = [line for line in lines if line]

    # Unir líneas con saltos de línea dobles
    clean_text = "\n\n".join(lines)

    return clean_text
