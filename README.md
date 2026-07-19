# Jogo de Batalha por Turnos (Player vs NPC)

Um jogo de batalha em turnos via terminal desenvolvido em Python puro, onde o jogador enfrenta um NPC controlado por decisões aleatórias.

## 🎮 O que o jogo faz

O script simula uma batalha por turnos entre o jogador (`Player`) e um oponente (`NPC das sombras`). Em cada round, o jogador escolhe entre atacar ou defender, enquanto o NPC faz sua escolha de forma aleatória. Os danos causados afetam primeiramente a defesa do personagem e, após a defesa ser esgotada, passam a reduzir a vida até que um dos participantes (ou ambos) seja derrotado.

Exemplo de execução no terminal:
```text
--- ROUND 1 ---
Player -> Vida: 100 | Defesa: 100
NPC    -> Vida: 100 | Defesa: 100
1 - Atacar | 2 - Defender: 1
Player: ATACAR | NPC: DEFENDER
Player atacou!
NPC defendeu!
```

## 🕹️ Como jogar

Ao iniciar a execução do programa, a cada round o terminal solicitará a sua ação através do input de texto:

- Digite `1` para **Atacar**: causa dano aleatório (entre 15 e 35) ao NPC.
- Digite `2` para **Defender**: o jogador assume postura defensiva no turno.
- Qualquer outro caractere/número digitado retornará uma mensagem de ação inválida e solicitará a entrada novamente sem avançar o turno.

## 🐍 Conceitos de Python usados

- **Dicionários**: Utilizados nas variáveis `player`, `inimigo` e `historico` para armazenar as estatísticas dos personagens (`nome`, `vida`, `defesa`) e registrar o progresso das rodadas.
- **Funções**: Aplicadas em `calcular_dano()`, `atacar()` e `escolher_acao_player()` para separar e organizar as responsabilidades do jogo, como cálculo de dano, aplicação de ataques e captura de entrada do usuário.
- **Módulos**: Importação do módulo `random` para gerar valores de dano aleatórios em `random.randint()` e definir a ação do NPC com `random.choice()`, além do módulo `math`.
- **Estruturas de repetição e condicionais**: Utilização do laço `while` para manter a batalha ativa enquanto a vida dos personagens for maior que zero, combinado com condicionais `if/elif/else` para validação do input do usuário, lógica do combate e checagem do vencedor.

## 💻 Como executar localmente

### Requisitos
- Python 3.x instalado na máquina.

### Passos para execução
1. Clone este repositório ou baixe o arquivo `.py` com o código do jogo.
2. Abra o terminal ou prompt de comando na pasta onde o arquivo está localizado.
3. Execute o comando:

```bash
python main.py
```
*(Substitua `main.py` pelo nome exato do seu arquivo Python)*

## 🚀 Possíveis melhorias futuras

- **Sistema de itens e poções**: Permitir que o jogador use itens para recuperar pontos de vida ou defesa durante o combate.
- **Múltiplos inimigos ou classes**: Adicionar diferentes tipos de NPCs com atributos variados ou batalhas em sequência.
- **Mecanica especial para a ação Defender**: Fazer com que a escolha de defender reduza ou anule o dano recebido naquele round.
