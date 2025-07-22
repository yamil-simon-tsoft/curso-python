"""
Ejemplo con código problemático para demostrar las herramientas de calidad
"""
import os,sys,math
import datetime
import requests  # Esta importación no se usa


def mal_formateado(x,y,z):
    """Función mal formateada para mostrar Black"""
    if x>5:
        resultado=x*y+z
        return resultado
    else:return x+y


def funcion_con_problemas(numeros):
    """Función con varios problemas de calidad"""
    # Línea muy larga que viola PEP 8 (más de 79 caracteres) - esto es un ejemplo de línea demasiado larga para mostrar flake8
    total = 0
    for i in range(len(numeros)):  # Mal uso de range(len())
        if numeros[i] > 10:
            total += numeros[i]
    
    variable_no_usada = "esto no se usa"  # Variable no usada
    
    # Operación potencialmente peligrosa sin verificación
    resultado = total / 0  # División por cero
    
    return total


def funcion_sin_tipos(parametro):
    """Función sin type hints para mostrar MyPy"""
    if parametro == "numero":
        return 42
    else:
        return "texto"


# Código mal indentado y sin espacios
class MiClase:
 def __init__(self,nombre):
  self.nombre=nombre
 
 def metodo(self):
     return self.nombre.upper()


# Código al nivel del módulo sin if __name__ == "__main__"
print("Este código se ejecuta siempre")
resultado = mal_formateado(10, 2, 3)
print(f"Resultado: {resultado}")
