# Dungeon Phantom

# Contexto do Jogo

Em um futuro **nada distante**, o mundo foi tomado por zumbis famintos, ruas abandonadas e… um herói extremamente determinado (você).

O jogo se passa em um cenário **pós-apocalíptico**, onde criaturas infectadas vagam sem rumo enquanto o jogador tenta sobreviver o máximo de tempo possível.

## Seu objetivo é simples:

**não encoste nos zumbis e sobreviva o máximo de tempo possível.**

---

# Telas do Jogo

### Tela de Menu

A tela inicial contém:

- Título do jogo: **Dungeon Phantom**
- Botões:
    - `Start` → inicia o jogo
    - `SFX` → ativa/desativa efeitos sonoros
    - `Music` → ativa/desativa música de fundo
    - `Exit` → encerra o jogo

Interface simples e funcional para facilitar o uso.

![image.png](https://github.com/estacioFilho/imagesProjects/blob/main/image%201.png?raw=true)

---

### Tela Principal (Gameplay)

Na tela principal:

- O herói aparece no mapa
- Inimigos se movimentam automaticamente
- O score é exibido no canto superior
- Mensagem inicial de introdução do nível
- Fundo fixo (cenário)

![image2.png](https://github.com/estacioFilho/imagesProjects/blob/main/image.png?raw=true)

Quando o herói colide com um inimigo:

> GAME OVER
> 

![image3.png](https://github.com/estacioFilho/imagesProjects/blob/main/image%202.png?raw=true)

---

## Objetivo do Jogo

O objetivo é:

> Sobreviver o maior tempo possível sem tocar nos inimigos.
> 
- A cada certo tempo, o jogador ganha pontos (score)
- Quanto mais tempo vivo, maior a pontuação
- Não existe fase final: é um jogo de sobrevivência (survival)

---

## Controles

### Movimento do personagem:

- `W` ou `↑` → mover para cima
- `S` ou `↓` → mover para baixo
- `A` ou `←` → mover para esquerda
- `D` ou `→` → mover para direita

### Pausa:

- `Enter` → Pausar o jogo

### Voltar ao Menu:

Para evitar perder a pontuação por acidente:

1. Primeiro pressione **Enter (Pause)**
2. Depois pressione **ESC** para voltar ao menu

Isso foi implementado propositalmente para evitar erros do jogador.

---

## Áudio

O jogo possui:

- Música de fundo (loop)
- Sons de movimento do herói
- Sons de movimento dos inimigos

Podem ser ativados/desativados individualmente:

- `SFX` → efeitos sonoros
- `Music` → música

---

## Ferramentas Utilizadas

- **Python 3**
- **PgZero (pgzrun)**
- Bibliotecas permitidas:
    - `math`
    - `random`
    - `pygame.Rect`

Ferramentas principais:

- PgZero para renderização
- Sistema de grid para movimentação
- Sistema simples de IA para inimigos

---

## Estrutura do Código (Visão Geral)

O código foi organizado com classes para reaproveitamento e clareza:

### GameObject

Classe base para todos os personagens.

Responsável por:

- Animação de sprites
- Movimento suave (lerp)
- Desenho na tela
- Hitbox de colisão

Principais funções:

- `animate()` → alterna frames
- `smooth()` → suaviza movimento
- `draw()` → desenha o ator
- `hitbox` → retorna área de colisão reduzida

---

### Character

Herda de `GameObject`.

Responsável por:

- Movimento em grid
- Verificação de:
    - limites da tela
    - colisão com inimigos
    - colisão com área bloqueada (WALL_RECT)

Função principal:

- `try_move(dx, dy, blockers)`

---

### Enemy

Herda de `Character`.

Possui:

- Sistema de IA simples
- Persegue o jogador com chance de movimento aleatório
- Movimento baseado em tempo (`ai_timer`)

---

## Sistema de Estados do Jogo

O jogo utiliza `game_state`:

- `"MENU"`
- `"PLAYING"`
- `"PAUSED"`
- `"GAMEOVER"`

Isso garante:

- Controle de fluxo
- Separação clara de telas
- Código organizado

---

## Pontuação (Score)

- O score aumenta automaticamente com o tempo
- Atualizado por um contador (`score_timer`)
- Incentiva o jogador a sobreviver mais tempo

---

## Área Bloqueada (Wall Rect)

Existe uma área fixa (`WALL_RECT`) onde o jogador não pode andar.

Ela representa um objeto do cenário (ex: tanque de guerra), impedindo movimento sobre ele para manter coerência visual.
