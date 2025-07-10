import pytest
from funciones import suma, cuadrado, cuadrado_binomio

# Kevin Damian – Pruebas Unitarias
def test_suma_kevin():
    assert suma(5, 3) == 8

def test_cuadrado_kevin():
    assert cuadrado(4) == 16

def test_suma_negativos_kevin():
    assert suma(-2, -3) == -5

# Kevin Damian – Prueba de Integración
def test_integracion_cuadrado_binomio_kevin():
    """Verifica que cuadrado_binomio usa correctamente suma y cuadrado"""
    a, b = 7, 8
    resultado = cuadrado_binomio(a, b)
    esperado = cuadrado(a) + 2 * a * b + cuadrado(b)
    assert resultado == esperado
    assert resultado == 225

# Julieta Fretes – Pruebas Unitarias
def test_suma_julieta():
    assert suma(10, 5) == 15

def test_cuadrado_negativos_julieta():
    assert cuadrado(-6) == 36

# Julieta Fretes – Prueba de Integración
def test_integracion_cuadrado_binomio_julieta():
    """Verifica que cuadrado_binomio usa correctamente suma y cuadrado"""
    a, b = 1, 2
    resultado = cuadrado_binomio(a, b)
    esperado = cuadrado(a) + 2 * a * b + cuadrado(b)
    assert resultado == esperado
    assert resultado == 9
