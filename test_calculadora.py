from Calculadora import fatorial, subtracao, multiplicacao, raiz_quadrada, adicao, divisao, logaritmo_natural, logaritmo_base10, cosseno, tangente, seno


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


def test_divisao():
    assert divisao(10, 2) == 5


def test_divisao_por_zero():
    assert divisao(10, 0) == "Erro: Divisão por zero"


def test_logaritmo_natural():
    assert abs(logaritmo_natural(10) - 2.302585) < 0.0001


def test_logaritmo_natural_nao_positivo():
    assert logaritmo_natural(0) == "Erro: Logaritmo de número não positivo"


def test_logaritmo_base10():
    assert abs(logaritmo_base10(100) - 2.0) < 0.0001


def test_logaritmo_base10_zero():
    assert logaritmo_base10(0) == "Erro: Logaritmo de número não positivo"


def test_fatorial_negativo():
    assert fatorial(-3) == "Erro: Fatorial de número negativo"


def test_cosseno_de_60_graus():
    assert abs(cosseno(60) - 0.5) < 0.0001


def test_tangente_de_45_graus():
    assert abs(tangente(45) - 1.0) < 0.0001


def test_seno_de_30_graus():
    assert abs(seno(30) - 0.5) < 0.0001