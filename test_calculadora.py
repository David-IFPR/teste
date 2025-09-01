import pytest
from calculadora import somar, subtrair, multiplicar, dividir

# Testes para somar
def test_somar_positivos():
    assert somar(2, 3) == 5

def test_somar_negativos():
    assert somar(-2, -3) == -5

def test_somar_zero():
    assert somar(0, 5) == 5

# Testes para subtrair
def test_subtrair_positivos():
    assert subtrair(5, 3) == 2

def test_subtrair_negativos():
    assert subtrair(-5, -3) == -2

def test_subtrair_zero():
    assert subtrair(0, 5) == -5

# Testes para multiplicar
def test_multiplicar_positivos():
    assert multiplicar(4, 3) == 12

def test_multiplicar_negativos():
    assert multiplicar(-2, 3) == -6

def test_multiplicar_zero():
    assert multiplicar(0, 5) == 0

# Testes para dividir
def test_dividir_positivos():
    assert dividir(10, 2) == 5

def test_dividir_negativos():
    assert dividir(-10, 2) == -5

def test_dividir_zero():
    with pytest.raises(ValueError):
        dividir(10, 0)
