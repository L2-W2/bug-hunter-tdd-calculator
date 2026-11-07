from Calculadora import fatorial, subtracao, multiplicacao, raiz_quadrada, adicao


def test_fatorial_de_5():
    assert fatorial(5) == 120


def test_fatorial_de_0():
    assert fatorial(0) == 1


def test_fatorial_de_1():
    assert fatorial(1) == 1


def test_subtracao():
    assert subtracao(5, 3) == 2


def test_multiplicacao():
    assert multiplicacao(4, 3) == 12


def test_raiz_quadrada():
    assert raiz_quadrada(16) == 4.0


def test_raiz_quadrada_negativa():
    assert raiz_quadrada(-4) == "Erro: Raiz quadrada de número negativo"

def test_adicao():
    assert adicao(2, 3) == 5