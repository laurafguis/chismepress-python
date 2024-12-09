import os
import markdown # type: ignore
from jinja2 import Environment, FileSystemLoader # type: ignore

class FileHandler:
    def __init__(self, template_dir):
        self.env = Environment(loader=FileSystemLoader(template_dir))

    def convert_markdown_to_html(self, markdown_content):
        try:
            return markdown.markdown(markdown_content)
        except Exception as e:
            raise ValueError(f"Error al convertir Markdown a HTML: {e}")

    def render_html(self, template_name, title, content):
        try:
            template = self.env.get_template(template_name)
            return template.render(title=title, content=content)
        except Exception as e:
            raise ValueError(f"Error al renderizar la plantilla {template_name}: {e}")

    def process_single_file(self, markdown_file, output_dir, template_name):
        os.makedirs(output_dir, exist_ok=True)
        try:
            with open(markdown_file, 'r', encoding='utf-8') as f:
                markdown_content = f.read()

            html_content = self.convert_markdown_to_html(markdown_content)
            rendered_html = self.render_html(template_name, title=os.path.basename(markdown_file), content=html_content)

            output_path = os.path.join(output_dir, os.path.basename(markdown_file).replace(".md", ".html"))
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(rendered_html)

            print(f"Archivo convertido: {output_path}")
        except Exception as e:
            print(f"Error al procesar el archivo {markdown_file}: {e}")

    def process_files_from_directory(self, markdown_dir, output_dir, template_name):
        os.makedirs(output_dir, exist_ok=True)
        for root, _, files in os.walk(markdown_dir):
            for file in files:
                if file.endswith(".md"):
                    markdown_file = os.path.join(root, file)
                    self.process_single_file(markdown_file, output_dir, template_name)

    def read_file(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            raise ValueError(f"Error al leer el archivo {file_path}: {e}")

    def write_file(self, file_path, content):
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
        except Exception as e:
            raise ValueError(f"Error al escribir en el archivo {file_path}: {e}")

    def get_template(self, template_name):
        try:
            return self.env.get_template(template_name)
        except Exception as e:
            raise ValueError(f"Error al obtener la plantilla {template_name}: {e}")
