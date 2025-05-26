import pgzrun
import random
import math
from pygame import Rect

WIDTH = 800
HEIGHT = 600


COR_FUNDO = (26, 32, 44)    
COR_TEXTO = (255, 255, 255) 
COR_BOTAO_INICIAR = (139, 92, 246) 
COR_BOTAO_OPCOES = (59, 130, 246)  
COR_BOTAO_SAIR = (239, 68, 68)     
COR_BOTAO_HOVER = (120, 70, 220)   
COR_BOTAO_HOVER_AZUL = (37, 99, 235) 
COR_BOTAO_HOVER_VERMELHO = (220, 38, 38) 

MENU = 0
JOGO = 1
OPCOES = 2
SAIR = 3

estado_atual = MENU

musica_iniciada = False


botoes = {
    "iniciar": {
        "rect": Rect((WIDTH // 2 - 150, HEIGHT // 2 - 80), (300, 60)),
        "text": "Iniciar Jogo",
        "color": COR_BOTAO_INICIAR,
        "hover_color": COR_BOTAO_HOVER,
        "action": lambda: mudar_estado(JOGO)
    },
    "opcoes": {
        "rect": Rect((WIDTH // 2 - 150, HEIGHT // 2 + 0), (300, 60)),
        "text": "Opções",
        "color": COR_BOTAO_OPCOES,
        "hover_color": COR_BOTAO_HOVER_AZUL,
        "action": lambda: mudar_estado(OPCOES)
    },
    "sair": {
        "rect": Rect((WIDTH // 2 - 150, HEIGHT // 2 + 80), (300, 60)),
        "text": "Sair",
        "color": COR_BOTAO_SAIR,
        "hover_color": COR_BOTAO_HOVER_VERMELHO,
        "action": lambda: mudar_estado(SAIR)
    }
}

mensagem_box_texto = ""
mensagem_box_tempo = 0
MENSAGEM_DURACAO = 3 * 60 


def iniciar_musica_fundo():
    """Toca a música de fundo em loop."""
    global musica_iniciada
    if not musica_iniciada:
        try:
            music.play("background.ogg", -1)
            music.set_volume(0.5)
            musica_iniciada = True
            print("Música de fundo iniciada.")
        except Exception as e:
            print(f"Erro ao iniciar música de fundo: {e}")
            exibir_mensagem("Erro ao carregar música!", "error")

def tocar_efeito_clique():
    """Toca o efeito sonoro de clique."""
    try:
        sounds.click.play()
        print("Efeito sonoro de clique tocado.")
    except Exception as e:
        print(f"Erro ao tocar efeito de clique: {e}")
        exibir_mensagem("Erro ao tocar som de clique!", "error")

# --- Funções do Jogo ---

# Função para mudar o estado do jogo
def mudar_estado(novo_estado):
    global estado_atual
    estado_atual = novo_estado
    print(f"Estado do jogo alterado para: {novo_estado}")
    # Exibe uma mensagem na caixa de mensagem
    if novo_estado == JOGO:
        exibir_mensagem("Iniciando o jogo...", "info")
    elif novo_estado == OPCOES:
        exibir_mensagem("Abrindo opções...", "info")
    elif novo_estado == SAIR:
        exibir_mensagem("Saindo do jogo...", "info")
        music.stop()

# Função para exibir mensagens na caixa de mensagem
def exibir_mensagem(mensagem, tipo):
    global mensagem_box_texto, mensagem_box_tempo
    mensagem_box_texto = mensagem
    mensagem_box_tempo = MENSAGEM_DURACAO
    print(f"Mensagem: {mensagem} (Tipo: {tipo})") # Para depuração

# Função de desenho principal do PG Zero
def draw():
    screen.fill(COR_FUNDO) # Preenche a tela com a cor de fundo

    # Garante que a música comece a tocar assim que a tela for desenhada
    iniciar_musica_fundo()

    if estado_atual == MENU:
        # Desenha o título do jogo
        screen.draw.text("Meu Jogo Incrível", center=(WIDTH // 2, HEIGHT // 2 - 200),
                         fontsize=70, color=COR_TEXTO,
                         shadow=(2, 2), scolor=(0,0,0,100)) # Adiciona uma sombra simples

        # Desenha os botões
        for nome_botao, botao in botoes.items():
            cor_atual = botao["color"]
            # Verifica se o mouse está sobre o botão para mudar a cor
            if botao["rect"].collidepoint(mouse.get_pos()):
                cor_atual = botao["hover_color"]

            screen.draw.filled_rect(botao["rect"], cor_atual)
            screen.draw.text(botao["text"], center=botao["rect"].center,
                             fontsize=36, color=COR_TEXTO)

        # Desenha a caixa de mensagem, se houver uma mensagem ativa
        if mensagem_box_texto:
            screen.draw.text(mensagem_box_texto, center=(WIDTH // 2, HEIGHT - 100),
                             fontsize=30, color=(144, 238, 144)) # Verde claro para mensagens

    elif estado_atual == JOGO:
        screen.draw.text("Bem-vindo ao Jogo!", center=(WIDTH // 2, HEIGHT // 2),
                         fontsize=50, color=COR_TEXTO)
        screen.draw.text("Pressione ESC para voltar ao menu", center=(WIDTH // 2, HEIGHT // 2 + 50),
                         fontsize=30, color=COR_TEXTO)
    elif estado_atual == OPCOES:
        screen.draw.text("Menu de Opções", center=(WIDTH // 2, HEIGHT // 2),
                         fontsize=50, color=COR_TEXTO)
        screen.draw.text("Pressione ESC para voltar ao menu", center=(WIDTH // 2, HEIGHT // 2 + 50),
                         fontsize=30, color=COR_TEXTO)
    elif estado_atual == SAIR:
        screen.draw.text("Obrigado por jogar!", center=(WIDTH // 2, HEIGHT // 2),
                         fontsize=50, color=COR_TEXTO)
        screen.draw.text("Fechando o jogo...", center=(WIDTH // 2, HEIGHT // 2 + 50),
                         fontsize=30, color=COR_TEXTO)

# Função de atualização principal do PG Zero
def update(dt):
    global mensagem_box_tempo
    if mensagem_box_tempo > 0:
        mensagem_box_tempo -= 1
        if mensagem_box_tempo == 0:
            global mensagem_box_texto
            mensagem_box_texto = ""

# Função de evento de clique do mouse do PG Zero
def on_mouse_down(pos):
    global estado_atual
    if estado_atual == MENU:
        for nome_botao, botao in botoes.items():
            if botao["rect"].collidepoint(pos):
                tocar_efeito_clique() # Toca o som de clique ao interagir com o botão
                botao["action"]() # Executa a ação associada ao botão clicado
    # Se estiver em JOGO ou OPCOES, o clique do mouse pode ter outras funções,
    # mas para este exemplo, apenas o menu responde.

# Função de evento de tecla pressionada do PG Zero
def on_key_down(key):
    global estado_atual
    if estado_atual == JOGO or estado_atual == OPCOES:
        if key == keys.ESCAPE:
            mudar_estado(MENU)
            exibir_mensagem("Voltando ao menu...", "info")
            tocar_efeito_clique()