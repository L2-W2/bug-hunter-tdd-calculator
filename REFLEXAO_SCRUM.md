# Reflexão sobre o processo com Scrum

## Como o Scrum apareceu na atividade

Como a atividade foi individual, tratei o trabalho como uma única sprint, com mim mesmo nos papéis de Product Owner, Scrum Master e desenvolvedor.

- **Meta da sprint:** identificar defeitos na calculadora, relatá-los e corrigir um deles com TDD, entregando tudo no GitHub até 09/11/2026.
- **Product Backlog:** a lista de 11 bugs do arquivo `Bugs.md`, ordenada por severidade.
- **Sprint Backlog:** o bug escolhido para a sprint, o BUG-03 (fatorial sempre devolve 0), mais a preparação necessária (BUG-11, que impedia os testes automatizados).
- **Incremento:** o repositório com o relatório de bugs, o código corrigido, os testes e as evidências.
- **Sprint Review:** rodei todos os testes (7 passando) e conferi o repositório no GitHub antes de entregar.
- **Retrospectiva:** descrita abaixo.

## O que funcionou

- Dividir o trabalho em etapas pequenas (estudo, preparação, caça aos bugs, relatório, TDD, entrega) deixou claro o que faltava a cada momento.
- Commits pequenos, um por fase do TDD (Red, Green, Refactor), deixaram o histórico fácil de entender e de desfazer em caso de erro.
- Escolher um único bug para corrigir, em vez de tentar corrigir todos, manteve a sprint dentro do prazo.

## O que deu errado ou pode melhorar

- Ao fazer o refactor, colei o docstring no lugar errado do arquivo. O `git diff` mostrou o erro antes do commit, e isso reforçou o valor de conferir as mudanças antes de commitar.
- Descobri tarde que o menu executava ao importar o arquivo (BUG-11), o que impedia os testes. Planejar a preparação do ambiente de testes no início teria poupado tempo.
- Deixei a documentação e a coleta de evidências para o fim. Na próxima sprint, registraria cada bug e o print no momento em que o encontro.

## Próxima sprint

Os bugs restantes continuam no backlog, em ordem de prioridade: os de severidade alta (BUG-01, BUG-02, BUG-05, BUG-06, BUG-09 e BUG-10) vêm primeiro, depois os de severidade média (BUG-04, BUG-07 e BUG-08). Cada um seria corrigido com o mesmo ciclo TDD, e os testes de regressão criados nesta sprint continuariam servindo de proteção.

## O que aprendi

O TDD muda a ordem de pensar: o teste que falha define o comportamento esperado antes da correção, e o teste passando é a prova de que o bug acabou. O Scrum ajudou a manter o foco em entregar um incremento funcional em vez de tentar resolver tudo de uma vez.