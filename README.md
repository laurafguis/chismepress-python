# ChismePress - Generador de Sitios Estáticos

ChismePress es un generador de sitios estáticos construido en Python. Permite convertir archivos Markdown en páginas HTML utilizando plantillas Jinja2 para un diseño estructurado y consistente.

## Índice

1. [Introducción](#introducción)
2. [Requisitos](#requisitos)
3. [Instalación](#instalación)
4. [Estructura del Proyecto](#estructura-del-proyecto)
5. [Uso](#uso)
   - [Desde la terminal](#desde-la-terminal)
6. [Funciones Implementadas](#funciones-implementadas)
7. [Pruebas](#pruebas)
   - [Pruebas en `test_file_handler.py`](#pruebas-en-test_file_handlerpy)
   - [Pruebas en `test_main.py`](#pruebas-en-test_mainpy)
8. [Ejecutar las Pruebas](#ejecutar-las-pruebas)

---

## Introducción

Los generadores de sitios estáticos (Static Site Generators o SSGs) convierten archivos Markdown en HTML para construir sitios web rápidos, seguros y fáciles de desplegar. ChismePress es una solución sencilla y eficiente que sigue este principio.

### Características principales:

- Conversión de Markdown a HTML.
- Uso de plantillas dinámicas mediante Jinja2.
- Manejo de múltiples archivos Markdown en un directorio.

---

## Requisitos

- Python 3.7 o superior.
- Librerías necesarias:
  - `markdown`
  - `jinja2`
  - `argparse`

Instálalas con:

```bash
pip install markdown jinja2 argparse
```

## Instalación
Clona este repositorio:
**git clone https://github.com/laurafguis/chismepress-python.git**

```bash
cd chismepress
```

Asegúrate de que las dependencias estén instaladas:
```bash
pip install -r requirements.txt
```

## Estructura del Proyecto

chismepress/
├── main.py              # Archivo principal para ejecutar la aplicación
├── templates/           # Contiene las plantillas HTML
│   └── default.html     # Plantilla predeterminada
├── docs/                # Archivos Markdown de ejemplo
├── output/              # Directorio donde se generan los archivos HTML
├── utils/               # Funciones auxiliares
│   └── file_handler.py  # Gestión de archivos y conversiones

## Uso
Convertir un solo archivo Markdown en HTML:
**python main.py ./docs/contacto.md ./output**

Convertir todos los archivos Markdown en un directorio:
**python main.py ./docs ./output***

## Argumento
markdown_dir: Ruta al archivo o directorio con los archivos Markdown.
output_dir: Directorio donde se guardarán los archivos HTML generados.
template_name: Ruta a la plantilla Jinja2 que se utilizará.

**python main.py ./docs ./output ./templates/default.html**


## Funciones Implementadas

**convert_markdown_to_html(markdown_content)**
Convierte el contenido Markdown en HTML utilizando la librería markdown.

Parámetros:
        `markdown_content (str)`: Texto en formato Markdown.
Retorno:
        HTML generado.
**render_html(template_path, title, content)**
Renderiza el HTML utilizando una plantilla Jinja2.

Parámetros:
        `template_path (str)`: Ruta a la plantilla Jinja2.
        `title (str)`: Título de la página (nombre del archivo Markdown).
        `content (str)`: Contenido HTML generado.
Retorno:
        HTML renderizado.
        
**process_single_file(markdown_file, output_dir, template_name)**
Convierte un solo archivo Markdown en HTML y lo guarda en el directorio especificado.

Parámetros:
        `markdown_file (str)`: Ruta al archivo Markdown.
        `output_dir (str)`: Directorio de salida.
        `template_name (str)`: Plantilla a utilizar para renderizar el HTML.

**process_files_from_directory(markdown_dir, output_dir, template_name)**

Convierte todos los archivos Markdown en un directorio en HTML.

Parámetros:
        `markdown_dir (str)`: Ruta al directorio con archivos Markdown.
        `output_dir (str)`: Directorio de salida.
        `template_name (str)`: Plantilla a utilizar para renderizar los archivos.

## Pruebas

Las pruebas se han implementado utilizando `pytest` y `unittest` para asegurar que todas las funcionalidades del proyecto funcionan correctamente. A continuación se describen las pruebas implementadas:

### Pruebas en `test_file_handler.py`

**test_convert_markdown_to_html**:
- Prueba que el contenido Markdown se convierta correctamente a HTML.
- Verifica que el HTML generado contenga los elementos esperados.

**test_process_single_file**:
- Prueba el procesamiento de un archivo Markdown a HTML.
- Verifica que el archivo HTML se genere correctamente y contenga el contenido esperado.

**test_process_files_from_directory**:
- Prueba el procesamiento de múltiples archivos Markdown en un directorio.
- Verifica que todos los archivos HTML se generen correctamente y contengan el contenido esperado.

**test_read_file**:
- Prueba la lectura de un archivo.
- Verifica que el contenido del archivo leído sea el esperado.

**test_write_file**:
- Prueba la escritura de un archivo.
- Verifica que el archivo se escriba correctamente y contenga el contenido esperado.

**test_get_template**:
- Prueba la obtención de una plantilla Jinja2.
- Verifica que la plantilla se obtenga correctamente desde el directorio de plantillas.

### Pruebas en `test_main.py`

**test_generate_output**:
- Prueba que los archivos Markdown se conviertan a HTML correctamente.
- Verifica que el archivo HTML se genere en el directorio de salida especificado.

**test_main_help**:
- Prueba que el comando `--help` funcione correctamente.
- Verifica que el mensaje de ayuda contenga las secciones esperadas.

## Ejecutar las Pruebas

Para ejecutar todas las pruebas, utiliza el siguiente comando:
```bash
pytest
```
