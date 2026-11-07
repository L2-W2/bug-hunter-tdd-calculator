# Relato da Experiência com Scrum e TDD na Atividade

## Como o Scrum entrou na jogada

Como essa atividade foi individual, precisei dar meus "pulos" dividindo o trabalho em duas sprints, acumulando os papéis de Product Owner, Scrum Master e desenvolvedor (o que rendeu bons momentos de conversar sozinho sobre prioridades). A Sprint 1 focou no que o professor pediu direto: relatar os bugs da calculadora e corrigir um deles usando TDD. Já na Sprint 2, limpei o restante do backlog aplicando exatamente o mesmo método.

---

## Sprint 1 — Foco na Entrega Inicial

- **Meta da sprint:** achar os defeitos na calculadora, documentar tudo e corrigir um dos bugs com TDD, subindo o repositório organizado para o GitHub até 09/11/2026.
- **Product Backlog:** a lista original de 11 bugs do arquivo `Bugs.md`, organizada por ordem de severidade.
- **Sprint Backlog:** escolhi o BUG-03 (o fatorial que teimava em devolver zero) e o BUG-11 como preparação urgente, já que ele impedia os testes automatizados de rodarem.
- **Incremento:** repositório redondinho no GitHub com o relatório de bugs, código corrigido, testes rodando e evidências salvas.
- **Sprint Review:** rodei todos os testes (fiquei com 7 passando) e conferi o repositório antes de fechar a entrega.

### Retrospectiva

**O que funcionou bem:** quebrar o trabalho em pedacinhos (estudar, preparar o terreno, caçar os bugs, relatar, aplicar TDD, entregar) tirou aquela sensação de estar travado. Além disso, fazer commits bem pequenos, um para cada fase do TDD (Red, Green, Refactor), me ajudou várias vezes e deixou o histórico muito limpo. Focar em corrigir só um bug por vez evitou que eu me perdesse no prazo.

**O que deu ruim ou pode melhorar:** na hora do refactor, colei um docstring no lugar errado do arquivo. Por sorte o `git diff` mostrou o erro antes do commit, o que me ensinou a sempre dar aquela conferida de segurança. Outra falha foi descobrir tarde demais que o menu rodava sozinho na importação (o BUG-11): se eu tivesse preparado o ambiente de testes logo no começo, teria economizado um bom tempo. Por fim, deixei para documentar e tirar prints no final. Na próxima, é registrar na hora em que o bug aparece.

### Planejamento da Sprint 2

Os outros bugs ficaram esperando no backlog. Decidi seguir a fila da severidade: primeiro os mais críticos (BUG-01, 02, 05, 06, 09 e 10) e depois os de severidade média (BUG-04, 07 e 08). O plano era o mesmo ciclo de TDD, usando os testes da Sprint 1 como um "seguro de vida" para garantir que nada quebraria no caminho.

---

## Sprint 2 — Faxina Geral no Backlog

- **Meta da sprint:** dar cabo dos 9 bugs restantes usando TDD, sem quebrar os testes anteriores, mantendo a documentação atualizada no GitHub. Data: 07/11/2026.
- **Product Backlog:** os 9 bugs que ainda estavam abertos no `Bugs.md`.
- **Sprint Backlog:** 7 ciclos de TDD no total. Na prática, juntei os bugs que moravam na mesma função para ganhar tempo: o BUG-06 e o BUG-07 na mesma tacada de logaritmo base 10; o BUG-09 e o BUG-10 juntos no cosseno e na tangente; e deixei o seno por último porque ele precisava da opção 10 do menu ligada. A ordem acabou sendo: BUG-01, BUG-02, BUG-05, BUG-06/07, BUG-04, BUG-09/10 e, por fim, o BUG-08.
- **Incremento:** código com todos os 11 bugs resolvidos, 18 testes automatizados passando, `Bugs.md` atualizado com o histórico de cada correção e a pasta de evidências completa, com os prints de Red e Green.
- **Sprint Review:** rodei o `pytest` a cada ciclo (a contagem subiu para 8, 10, 12, 14, 15, 17 e finalmente 18 testes passando), testei a opção 10 do menu manualmente e conferi se o GitHub estava atualizado.

### Retrospectiva

**O que funcionou bem:** repetir a mesma receita de bolo (escrever o teste que falha, commit, arrumar o código, teste passa, commit e push) deixou o processo muito mais ágil no final. O hábito de só dar push com todos os testes passando evitou subir código quebrado para o repositório. E os testes antigos foram ótimos guardas-costas: a cada alteração, eles rodavam para provar que o que já funcionava continuava inteiro. Agrupar funções parecidas também fluiu bem, sem perder o rigor técnico.

**O que deu ruim ou pode melhorar:** escorreguei ao rodar o `pytest` sem salvar o arquivo de testes antes, e o resultado mostrou a versão antiga. Aprendi a olhar a bolinha na aba do editor para ver se há alterações pendentes. O menu continua usando `input`, então ficou sem teste automatizado (uma boa ideia para o futuro seria separar a lógica ou simular as entradas). Outra lição: ao revisar os prints, notei que uma das imagens mostrava nomes de usuário de outro app. Editei a imagem antes de finalizar e, na próxima, olho com mais cuidado antes de publicar em repositório aberto. Por fim, no caso do cosseno, do seno e da tangente, tive que decidir sozinho que o ângulo seria em graus, porque o menu pedia isso. Numa situação real de trabalho, eu teria que alinhar essa dúvida com o Product Owner antes de codar.

---

## O que fica de aprendizado

Fazer TDD mexe com a nossa lógica: primeiro você desenha o comportamento que espera através de um teste que quebra, e ver ele passar depois é a prova real de que o problema foi resolvido. Fazer isso em vários bugs na sequência me deu muita segurança, porque a rede de testes avisa na hora se uma correção estragar outra parte do sistema. No fim das contas, usar o Scrum, mesmo sozinho, ajudou a manter o foco em entregar valor em partes (primeiro a entrega da atividade, depois o resto), garantindo que o código estivesse sempre funcionando e pronto para rodar.