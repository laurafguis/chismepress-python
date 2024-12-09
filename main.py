import argparse
import os
from utils.file_handler import FileHandler

DEFAULT_TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')
DEFAULT_TEMPLATE_NAME = "default.html"

def main():
    parser = argparse.ArgumentParser(description="ChismePress: Un generador de sitios estáticos.")
    parser.add_argument('markdown_dir', help="Ruta a un directorio que contiene archivos Markdown o a un archivo Markdown individual")
    parser.add_argument('output_dir', help="Directorio donde se guardarán los archivos HTML convertidos")

    args = parser.parse_args()

    if not os.path.exists(args.markdown_dir):
        print(f"Error: La ruta '{args.markdown_dir}' no existe.")
        return
    if not os.path.exists(DEFAULT_TEMPLATE_DIR):
        print(f"Error: El directorio de plantillas '{DEFAULT_TEMPLATE_DIR}' no existe.")
        return
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir, exist_ok=True)

    file_handler = FileHandler(DEFAULT_TEMPLATE_DIR)

    if os.path.isdir(args.markdown_dir):
        print(f"Procesando directorio: {args.markdown_dir}")
        file_handler.process_files_from_directory(args.markdown_dir, args.output_dir, DEFAULT_TEMPLATE_NAME)
    elif os.path.isfile(args.markdown_dir):
        print(f"Procesando archivo individual: {args.markdown_dir}")
        file_handler.process_single_file(args.markdown_dir, args.output_dir, DEFAULT_TEMPLATE_NAME)
    else:
        print(f"Entrada inválida: '{args.markdown_dir}' no es un archivo ni un directorio válido.")

if __name__ == "__main__":
    main()
