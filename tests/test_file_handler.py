import os
import pytest # type: ignore
from utils.file_handler import FileHandler

# Variables globales para pruebas
TEST_TEMPLATE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "templates"))
TEST_TEMPLATE_FILE = "default.html"
TEST_OUTPUT_DIR = "tests/output"

@pytest.fixture
def file_handler():
    """Fixture para inicializar la clase FileHandler."""
    return FileHandler(template_dir=TEST_TEMPLATE_DIR)

@pytest.fixture
def setup_environment(tmp_path):
    """Crea el entorno de prueba con archivos y directorios temporales."""
    # Crear archivo Markdown de prueba
    markdown_file = tmp_path / "test.md"
    markdown_file.write_text("# Título de Prueba\nEsto es un párrafo de prueba.", encoding="utf-8")

    # Crear directorio temporal para la salida
    output_dir = tmp_path / "output"
    output_dir.mkdir()

    # Crear directorio temporal para plantillas
    template_dir = tmp_path / "templates"
    template_dir.mkdir()
    (template_dir / TEST_TEMPLATE_FILE).write_text("""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>{{ title }}</title>
    </head>
    <body>
        <h1>{{ title }}</h1>
        <div>{{ content|safe }}</div>
    </body>
    </html>
    """)

    return markdown_file, output_dir, template_dir

def test_convert_markdown_to_html(file_handler):
    """Prueba que Markdown se convierta correctamente a HTML."""
    markdown_content = "# Título de Prueba\nEsto es un párrafo de prueba."
    html_content = file_handler.convert_markdown_to_html(markdown_content)
    assert "<h1>Título de Prueba</h1>" in html_content
    assert "<p>Esto es un párrafo de prueba.</p>" in html_content

def test_process_single_file(file_handler, setup_environment):
    """Prueba el procesamiento de un archivo Markdown a HTML."""
    markdown_file, output_dir, template_dir = setup_environment

    # Actualizar la ruta de plantillas
    file_handler.env.loader.searchpath = [str(template_dir)]

    # Procesar el archivo Markdown
    file_handler.process_single_file(str(markdown_file), str(output_dir), TEST_TEMPLATE_FILE)

    # Verificar que el archivo HTML fue generado
    output_file = output_dir / "test.html"
    assert output_file.exists()

    # Verificar el contenido del archivo HTML
    html_content = output_file.read_text(encoding="utf-8")
    assert "<h1>Título de Prueba</h1>" in html_content
    assert "<p>Esto es un párrafo de prueba.</p>" in html_content

def test_process_files_from_directory(file_handler, setup_environment):
    """Prueba el procesamiento de múltiples archivos Markdown en un directorio."""
    _, output_dir, template_dir = setup_environment
    markdown_dir = output_dir / "markdown"
    markdown_dir.mkdir()
    (markdown_dir / "test1.md").write_text("# Archivo 1\nContenido 1.", encoding="utf-8")
    (markdown_dir / "test2.md").write_text("# Archivo 2\nContenido 2.", encoding="utf-8")

    # Actualizar el directorio de plantillas
    file_handler.env.loader.searchpath = [str(template_dir)]

    # Procesar todos los archivos en el directorio
    file_handler.process_files_from_directory(str(markdown_dir), str(output_dir), TEST_TEMPLATE_FILE)

    # Verificar que ambos archivos HTML fueron generados
    output_file1 = output_dir / "test1.html"
    output_file2 = output_dir / "test2.html"
    assert output_file1.exists()
    assert output_file2.exists()

    # Verificar el contenido de los archivos HTML generados
    assert "<h1>Archivo 1</h1>" in output_file1.read_text(encoding="utf-8")
    assert "<h1>Archivo 2</h1>" in output_file2.read_text(encoding="utf-8")

def test_read_file(file_handler, setup_environment):
    """Prueba la lectura de un archivo."""
    markdown_file, _, _ = setup_environment
    content = file_handler.read_file(str(markdown_file))
    assert content == "# Título de Prueba\nEsto es un párrafo de prueba."

def test_write_file(file_handler, setup_environment):
    """Prueba la escritura de un archivo."""
    _, output_dir, _ = setup_environment
    output_file = output_dir / "test_output.html"
    content = "<h1>Prueba</h1><p>Contenido de prueba.</p>"
    file_handler.write_file(str(output_file), content)
    assert output_file.exists()
    assert output_file.read_text(encoding="utf-8") == content

def test_get_template(file_handler, setup_environment):
    """Prueba la obtención de una plantilla."""
    _, _, template_dir = setup_environment
    file_handler.env.loader.searchpath = [str(template_dir)]
    template = file_handler.get_template(TEST_TEMPLATE_FILE)
    assert template is not None
    assert template.filename == str(template_dir / TEST_TEMPLATE_FILE)
