"""
Módulo de utilidades generales.
Contiene funciones útiles que pueden ser reutilizadas en el proyecto.
"""

import math
from typing import List, Union

def calcular_area_circulo(radio: float) -> float:
    """
    Calcula el área de un círculo.
    
    Args:
        radio (float): El radio del círculo
        
    Returns:
        float: El área del círculo
    """
    if radio < 0:
        raise ValueError("El radio no puede ser negativo")
    return math.pi * radio ** 2

def es_numero_primo(numero: int) -> bool:
    """
    Verifica si un número es primo.
    
    Args:
        numero (int): El número a verificar
        
    Returns:
        bool: True si es primo, False en caso contrario
    """
    if numero < 2:
        return False
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            return False
    return True

def convertir_temperatura(temperatura: float, desde: str, hacia: str) -> float:
    """
    Convierte temperatura entre diferentes escalas.
    
    Args:
        temperatura (float): La temperatura a convertir
        desde (str): Escala de origen ('C', 'F', 'K')
        hacia (str): Escala de destino ('C', 'F', 'K')
        
    Returns:
        float: La temperatura convertida
    """
    escalas = ['C', 'F', 'K']
    if desde not in escalas or hacia not in escalas:
        raise ValueError("Las escalas deben ser 'C', 'F' o 'K'")
    
    # Convertir a Celsius primero
    if desde == 'F':
        celsius = (temperatura - 32) * 5/9
    elif desde == 'K':
        celsius = temperatura - 273.15
    else:
        celsius = temperatura
    
    # Convertir desde Celsius a la escala destino
    if hacia == 'F':
        return celsius * 9/5 + 32
    elif hacia == 'K':
        return celsius + 273.15
    else:
        return celsius

def obtener_estadisticas(numeros: List[Union[int, float]]) -> dict:
    """
    Calcula estadísticas básicas de una lista de números.
    
    Args:
        numeros (List[Union[int, float]]): Lista de números
        
    Returns:
        dict: Diccionario con estadísticas (promedio, mediana, mínimo, máximo)
    """
    if not numeros:
        raise ValueError("La lista no puede estar vacía")
    
    numeros_ordenados = sorted(numeros)
    n = len(numeros)
    
    return {
        'promedio': sum(numeros) / n,
        'mediana': numeros_ordenados[n//2] if n % 2 == 1 else 
                  (numeros_ordenados[n//2-1] + numeros_ordenados[n//2]) / 2,
        'minimo': min(numeros),
        'maximo': max(numeros),
        'total': len(numeros)
    }
