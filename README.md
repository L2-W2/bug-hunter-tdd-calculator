# Bug Hunter & TDD Calculator

Projeto da disciplina **Alta Qualidade em Software** (Contexto de Aprendizagem - Parada Obrigatória 2).

A partir de uma calculadora científica em Python que continha defeitos, o trabalho consistiu em **encontrar os bugs, relatá-los** e **corrigi-los com TDD** (Test-Driven Development), usando `pytest`, Git e GitHub. A reflexão sobre o processo foi feita com base no Scrum.

**Autor:** Lucas Wanderley

## Resultado

- 11 bugs identificados e documentados
- 11 bugs corrigidos
- 18 testes automatizados passando
- Histórico de commits com o ciclo Red → Green de cada correção

## Estrutura do repositório

| Arquivo / pasta | Conteúdo |
|---|---|
| `Calculadora.py` | Calculadora científica (código corrigido) |
| `test_calculadora.py` | Testes automatizados com `pytest` |
| `Bugs.md` | Relatório detalhado dos 11 bugs e das correções feitas com TDD |
| `REFLEXAO_SCRUM.md` | Reflexão sobre o processo, organizada em duas sprints |
| `evidencias/` | Prints dos bugs e dos ciclos de TDD (Red e Green) |

## Funcionalidades da calculadora

Menu de operações:

| Opção | Operação |
|---|---|
| 0 | Sair |
| 1 | Adição |
| 2 | Subtração |
| 3 | Multiplicação |
| 4 | Divisão |
| 5 | Potenciação |
| 6 | Raiz quadrada |
| 7 | Fatorial |
| 8 | Logaritmo natural (ln) |
| 9 | Logaritmo base 10 |
| 10 | Seno |
| 11 | Cosseno |
| 12 | Tangente |

Seno, cosseno e tangente recebem o ângulo em **graus**.

## Como executar

Requisitos: Python 3 e as bibliotecas `numpy` e `pytest`.

```
pip install numpy pytest
```

Para usar a calculadora:

```
python Calculadora.py
```

Para rodar os testes:

```
pytest
```

O resultado esperado é `18 passed`.

## Bugs encontrados e corrigidos

| ID | Bug | Status |
|---|---|---|
| BUG-01 | Adição devolve 2x + y | Resolvido |
| BUG-02 | Divisão por zero não tratada | Resolvido |
| BUG-03 | Fatorial sempre devolve 0 | Resolvido |
| BUG-04 | Fatorial sem validação de número negativo | Resolvido |
| BUG-05 | Logaritmo natural usa função inexistente (`np.ln`) | Resolvido |
| BUG-06 | Logaritmo base 10 usa `np.log` | Resolvido |
| BUG-07 | Logaritmo base 10 aceita o valor 0 | Resolvido |
| BUG-08 | Seno listado no menu, mas não implementado | Resolvido |
| BUG-09 | Cosseno chama função inexistente | Resolvido |
| BUG-10 | Tangente chama função inexistente | Resolvido |
| BUG-11 | Menu executa ao importar o arquivo | Resolvido |

O detalhamento de cada bug (localização, passos para reproduzir, resultado esperado e obtido, severidade e solução) está em [`Bugs.md`](Bugs.md).

## Como o TDD foi aplicado

Cada correção seguiu o mesmo ciclo:

1. **Red:** escrever um teste que descreve o comportamento correto e confirmar que ele falha (commit do teste).
2. **Green:** fazer a menor mudança possível no código para o teste passar (commit da correção e `push` somente com todos os testes passando).
3. **Refactor:** melhorar o código, quando necessário, sem alterar o comportamento.

Os testes criados também funcionam como proteção contra regressões: a cada correção, todos os testes anteriores continuaram passando.

As prints de cada etapa estão na pasta [`evidencias/`](evidencias/), e a reflexão sobre o processo está em [`REFLEXAO_SCRUM.md`](REFLEXAO_SCRUM.md).