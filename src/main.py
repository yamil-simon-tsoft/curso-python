"""
Archivo principal del proyecto Python.
Este es el punto de entrada de la aplicación.
"""

import sys
import os
from datetime import datetime

def main():
    """Función principal del programa."""
    print("¡Bienvenido a tu proyecto Python!")
    print(f"Fecha y hora actual: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Versión de Python: {sys.version}")
    print(f"Directorio actual: {os.getcwd()}")
    
    # Ejemplo de uso de funciones
    resultado = sumar_numeros(5, 3)
    print(f"Ejemplo de suma: 5 + 3 = {resultado}")
    
    # Ejemplo de trabajo con listas
    numeros = [1, 2, 3, 4, 5]
    cuadrados = calcular_cuadrados(numeros)
    print(f"Cuadrados de {numeros}: {cuadrados}")

def sumar_numeros(a, b):
    """
    Suma dos números.
    
    Args:
        a (int/float): Primer número
        b (int/float): Segundo número
        
    Returns:
        int/float: La suma de a y b
    """
    return a + b

def calcular_cuadrados(numeros):
    """
    Calcula el cuadrado de cada número en una lista.
    
    Args:
        numeros (list): Lista de números
        
    Returns:
        list: Lista con los cuadrados de los números
    """
    return [num ** 2 for num in numeros]

if __name__ == "__main__":
    """
    Esta línea verifica si el archivo se está ejecutando directamente.
    
    __name__ es una variable especial de Python que:
    - Contiene "__main__" cuando el archivo se ejecuta directamente
    - Contiene el nombre del módulo cuando el archivo es importado
    
    Esto permite que el código funcione como script ejecutable
    y también como módulo importable sin ejecutar main().
    
    Ejemplo práctico:
    - Si ejecutas: python main.py
      __name__ será "__main__" y se ejecutará main()
    
    - Si haces: import main
      __name__ será "main" y NO se ejecutará main()
    """
    main()
