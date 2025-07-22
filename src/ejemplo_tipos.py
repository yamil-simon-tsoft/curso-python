"""
Ejemplo con problemas de tipos para demostrar MyPy
"""
from typing import Union


def funcion_con_tipos(numero: int, texto: str) -> str:
    """Función bien tipada"""
    return f"{texto}: {numero}"


def funcion_problemas_tipos(parametro):
    """Función sin tipos que causa problemas"""
    if parametro == "numero":
        return 42  # Devuelve int
    else:
        return "texto"  # Devuelve str - Problema: tipos inconsistentes


def usar_funciones():
    """Demuestra problemas de tipos"""
    # Esto está bien tipado
    resultado1 = funcion_con_tipos(10, "Valor")
    
    # Esto causará problemas de tipos
    resultado2 = funcion_problemas_tipos("numero")
    
    # MyPy no puede inferir el tipo de resultado2
    # Si intentamos usarlo como string, puede fallar en runtime
    longitud = len(resultado2)  # Problema: resultado2 puede ser int o str
    
    return longitud


def division_sin_verificacion(a: int, b: int) -> float:
    """División que puede fallar"""
    return a / b  # Problema: b podría ser 0


# Ejemplo de uso problemático
resultado = funcion_problemas_tipos("algo")
print(resultado.upper())  # Error potencial: si resultado es int, no tiene .upper()
