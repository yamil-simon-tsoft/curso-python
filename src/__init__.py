"""
Paquete principal del curso de Python.

¿Qué es __init__.py?
- Es un archivo especial que convierte un directorio en un paquete Python
- Sin este archivo, Python no reconoce el directorio como importable
- Se ejecuta automáticamente cuando importas el paquete

Funciones principales:
1. Hacer que el directorio sea un paquete Python
2. Definir metadata del paquete (versión, autor, etc.)
3. Controlar qué se importa cuando usas "from paquete import *"
4. Inicializar el paquete (ejecutar código al importar)

Ejemplo práctico:
- Con __init__.py: ✅ import src.main
- Sin __init__.py: ❌ import src.main (Error!)
"""

# Metadata del paquete
__version__ = "1.0.0"
__author__ = "Tu Nombre"

# Importar funciones principales para fácil acceso
# Esto permite usar: from src import main
# En lugar de: from src.main import main
from .main import main, sumar_numeros, calcular_cuadrados

# Define qué se puede importar con "from src import *"
__all__ = ["main", "sumar_numeros", "calcular_cuadrados"]
