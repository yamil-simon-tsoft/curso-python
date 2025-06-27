"""
Tests para el módulo utils.
Contiene pruebas unitarias para las funciones de utilidades.
"""

import pytest
import math
import sys
import os

# Añadir el directorio src al path para poder importar módulos
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from utils import (
    calcular_area_circulo,
    es_numero_primo,
    convertir_temperatura,
    obtener_estadisticas
)

class TestCalcularAreaCirculo:
    """Pruebas para la función calcular_area_circulo."""
    
    def test_area_circulo_positivo(self):
        """Prueba con radio positivo."""
        radio = 5
        area_esperada = math.pi * 25
        assert calcular_area_circulo(radio) == area_esperada
    
    def test_area_circulo_cero(self):
        """Prueba con radio cero."""
        assert calcular_area_circulo(0) == 0
    
    def test_area_circulo_negativo(self):
        """Prueba que se lance excepción con radio negativo."""
        with pytest.raises(ValueError):
            calcular_area_circulo(-5)

class TestEsNumeroPrimo:
    """Pruebas para la función es_numero_primo."""
    
    def test_numeros_primos(self):
        """Prueba con números primos conocidos."""
        primos = [2, 3, 5, 7, 11, 13, 17, 19, 23]
        for primo in primos:
            assert es_numero_primo(primo) is True
    
    def test_numeros_no_primos(self):
        """Prueba con números no primos."""
        no_primos = [1, 4, 6, 8, 9, 10, 12, 15, 16]
        for no_primo in no_primos:
            assert es_numero_primo(no_primo) is False

class TestConvertirTemperatura:
    """Pruebas para la función convertir_temperatura."""
    
    def test_celsius_a_fahrenheit(self):
        """Prueba conversión de Celsius a Fahrenheit."""
        assert convertir_temperatura(0, 'C', 'F') == 32
        assert convertir_temperatura(100, 'C', 'F') == 212
    
    def test_fahrenheit_a_celsius(self):
        """Prueba conversión de Fahrenheit a Celsius."""
        assert convertir_temperatura(32, 'F', 'C') == 0
        assert convertir_temperatura(212, 'F', 'C') == 100
    
    def test_escala_invalida(self):
        """Prueba que se lance excepción con escala inválida."""
        with pytest.raises(ValueError):
            convertir_temperatura(100, 'X', 'C')

class TestObtenerEstadisticas:
    """Pruebas para la función obtener_estadisticas."""
    
    def test_estadisticas_basicas(self):
        """Prueba cálculo de estadísticas básicas."""
        numeros = [1, 2, 3, 4, 5]
        stats = obtener_estadisticas(numeros)
        
        assert stats['promedio'] == 3
        assert stats['mediana'] == 3
        assert stats['minimo'] == 1
        assert stats['maximo'] == 5
        assert stats['total'] == 5
    
    def test_lista_vacia(self):
        """Prueba que se lance excepción con lista vacía."""
        with pytest.raises(ValueError):
            obtener_estadisticas([])
