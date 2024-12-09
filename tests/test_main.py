import os
import subprocess
import unittest

class TestMain(unittest.TestCase):
    def test_generate_output(self):
        """Prueba que los archivos Markdown se conviertan a HTML correctamente."""
        # Crear un directorio temporal de prueba
        test_docs_dir = os.path.join(os.path.dirname(__file__), "test_docs")
        test_output_dir = os.path.join(os.path.dirname(__file__), "test_output")
        os.makedirs(test_docs_dir, exist_ok=True)
        os.makedirs(test_output_dir, exist_ok=True)

        # Crear un archivo Markdown de prueba
        test_markdown_path = os.path.join(test_docs_dir, "test.md")
        with open(test_markdown_path, "w", encoding="utf-8") as f:
            f.write("# Prueba\nEste es un archivo de prueba.")

        # Ejecutar el script con los argumentos correctos
        subprocess.run(
            ["python", "main.py", test_docs_dir, test_output_dir, "--template_dir", "templates", "--template_name", "default.html"]
        )

        # Verificar que el archivo HTML fue generado
        test_html_path = os.path.join(test_output_dir, "test.html")
        self.assertTrue(os.path.exists(test_html_path))

    def test_main_help(self):
        """Prueba que el comando --help funcione correctamente."""
        result = subprocess.run(["python", "main.py", "--help"], capture_output=True, text=True)
        print(result.stdout)  # Añadir impresión del resultado para depuración
        self.assertIn("ChismePress", result.stdout)
        self.assertIn("usage: main.py", result.stdout)
        self.assertIn("positional arguments:", result.stdout)
        self.assertIn("options:", result.stdout)

if __name__ == "__main__":
    unittest.main()
