"""
Este módulo configura el paquete para distribución.
"""
from setuptools import setup, find_packages

def requirements_analysis(filename):
    "lee el archivo de dependencias y devuelve sus líneas como una lista."
    with open(filename, encoding="UTF-8") as f:
        return f.read().splitlines()

setup(
    name = "inventory_management",
    version = "1.0",
    packages = find_packages(),
    include_package_data = True,
    install_requires = requirements_analysis('requirements.txt'),
    entry_points = {
        'console_scripts': [
            # Permite ejecutar `runserver` desde la línea de comandos
            'runserver=scripts.run_server:main'
        ]
    },
    author = "Renato",
    author_email = "racaroa1@upao.edu.pe",
    description = "Sistema de control de inventarios para la empresa Aquarela.",
    url = "https://github.com/AKr3n1/inventarios_aquarela.git",
    python_requires='>=3.12'
)
