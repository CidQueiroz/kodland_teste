# 🎮 Roguelike Simple Game - PgZero

Bem-vindo ao **Roguelike Simple Game**, um mini-jogo feito em Python com [PgZero](https://pygame-zero.readthedocs.io/en/stable/) onde você controla um herói azul e precisa escapar de inimigos vermelhos que se movem de forma imprevisível!

---

## 🕹️ Como Jogar

- **Movimente o herói** usando as setas do teclado.
- **Desvie dos inimigos vermelhos**: se for tocado, aparece uma tela de "Game Over" e o jogo reinicia.
- **Menu principal**:  
  - `Start Game` inicia o jogo.
  - `Sound On/Off` liga ou desliga a música e efeitos.
  - `Exit` fecha o jogo.

---

## ✨ Funcionalidades

- **Menu principal** com botões clicáveis.
- **Música de fundo** e efeitos sonoros.
- **Herói controlado pelo jogador**.
- **Inimigos com movimento aleatório** em seu território.
- **Detecção de colisão** e tela de Game Over.
- **Código limpo e comentado** para fácil entendimento.

---

## 📦 Instalação

1. **Clone este repositório:**
   ```bash
   git clone https://github.com/CidQueiroz/kodland_teste.git
   cd kodland_teste
   ```

2. **(Opcional) Crie um ambiente virtual:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install pgzero
   ```

4. **Adicione os arquivos de áudio:**
   - Música de fundo: `music/background.ogg`
   - Efeito de clique: `sounds/click.wav`

---

## ▶️ Como Rodar

Execute o jogo com:
```bash
pgzrun teste_jogo.py
```

---

## 📁 Estrutura de Pastas

```
.
├── teste_jogo.py
├── music
│   └── background.ogg
├── sounds
│   └── click.wav
```

---

## 📝 Créditos

- **Desenvolvimento:** Cidirclay Queiroz
- **Sons e músicas:** [Freesound](https://freesound.org/)

---

## 🚀 Dicas

- Você pode adicionar mais inimigos ou sprites personalizados na pasta `images`.
- Experimente trocar a música ou efeitos para deixar o jogo com a sua cara!

---

Divirta-se jogando e modificando! 😃