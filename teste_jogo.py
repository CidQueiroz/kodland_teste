import pgzrun
import random
import math
from pygame import Rect

WIDTH = 800
HEIGHT = 600

# Estados do jogo
STATE_MENU = "menu"
STATE_GAME = "game"
STATE_EXIT = "exit"

game_state = STATE_MENU
sound_on = True 

# Botões do menu principal
menu_buttons = [
    {"label": "Start Game", "rect": Rect((300, 200), (200, 50)), "action": "start"},
    {"label": "Sound On/Off", "rect": Rect((300, 270), (200, 50)), "action": "sound"},
    {"label": "Exit", "rect": Rect((300, 340), (200, 50)), "action": "exit"},
]

# Classe dos inimigos
class Enemy:
    def __init__(self, x, y, left_limit, right_limit, speed):
        self.x = x
        self.y = y
        self.left_limit = left_limit
        self.right_limit = right_limit
        self.top_limit = 50
        self.bottom_limit = HEIGHT - 50
        self.speed = speed
        self.dir_x = random.choice([-1, 1])
        self.dir_y = random.choice([-1, 1])
        self.change_dir_timer = random.randint(30, 90)

    def update(self):
        # Movimento aleatório dentro dos limites
        self.x += self.speed * self.dir_x
        self.y += self.speed * self.dir_y
        self.change_dir_timer -= 1

        if self.x > self.right_limit:
            self.x = self.right_limit
            self.dir_x = -1
        elif self.x < self.left_limit:
            self.x = self.left_limit
            self.dir_x = 1

        if self.y > self.bottom_limit:
            self.y = self.bottom_limit
            self.dir_y = -1
        elif self.y < self.top_limit:
            self.y = self.top_limit
            self.dir_y = 1

        if self.change_dir_timer <= 0:
            self.dir_x = random.choice([-1, 0, 1])
            self.dir_y = random.choice([-1, 0, 1])
            if self.dir_x == 0 and self.dir_y == 0:
                self.dir_x = 1
            self.change_dir_timer = random.randint(30, 90)

    def draw(self):
        screen.draw.filled_circle((self.x, self.y), 20, "red")

# Classe do herói controlado pelo jogador
class Hero:
    def __init__(self, x, y, speed=4):
        self.x = x
        self.y = y
        self.radius = 20
        self.speed = speed

    def update(self):
        # Movimento do herói pelo teclado
        if keyboard.left and self.x - self.radius > 0:
            self.x -= self.speed
        if keyboard.right and self.x + self.radius < WIDTH:
            self.x += self.speed
        if keyboard.up and self.y - self.radius > 0:
            self.y -= self.speed
        if keyboard.down and self.y + self.radius < HEIGHT:
            self.y += self.speed

    def draw(self):
        screen.draw.filled_circle((self.x, self.y), self.radius, "blue")

hero = Hero(WIDTH // 2, HEIGHT // 2)

# Lista de inimigos
enemies = [
    Enemy(200, 400, 150, 350, 2),
    Enemy(600, 300, 550, 750, 3)
]

# Função para tocar ou parar a música de fundo
def play_music():
    if sound_on:
        music.play('background')
        music.set_volume(0.5)
    else:
        music.stop()

# Função principal de desenho da tela
def draw():
    screen.clear()
    if game_state == STATE_MENU:
        draw_menu()
    elif game_state == STATE_GAME:
        hero.draw()
        for enemy in enemies:
            enemy.draw()

# Desenha o menu principal
def draw_menu():
    screen.draw.text("Main Menu", center=(WIDTH//2, 120), fontsize=60, color="yellow")
    for btn in menu_buttons:
        screen.draw.filled_rect(btn["rect"], "darkblue")
        screen.draw.text(btn["label"], center=btn["rect"].center, fontsize=36, color="white")
    sound_status = "ON" if sound_on else "OFF"
    screen.draw.text(f"Sound: {sound_status}", (10, HEIGHT-40), fontsize=30, color="white")

# Processa cliques do mouse no menu
def on_mouse_down(pos):
    global game_state, sound_on

    if game_state == STATE_MENU:
        for btn in menu_buttons:
            if btn["rect"].collidepoint(pos):
                if sound_on:
                    sounds.click.play()

                if btn["action"] == "start":
                    game_state = STATE_GAME
                elif btn["action"] == "sound":
                    sound_on = not sound_on
                    if sound_on:
                        play_music()
                        sounds.click.play()
                    else:
                        music.stop()
                elif btn["action"] == "exit":
                    exit()

# Atualiza a lógica do jogo a cada frame
def update(dt):
    global game_state
    
    if game_state == STATE_MENU:
        if sound_on and not music.is_playing('background'):
            play_music()
        if not sound_on and music.is_playing('background'):
            music.stop()
    
    if game_state == STATE_GAME:
        hero.update()
        for enemy in enemies:
            enemy.update()
            dist = math.hypot(hero.x - enemy.x, hero.y - enemy.y)
            if dist < hero.radius + 20: 
                game_state = STATE_MENU
                hero.x = WIDTH // 2
                hero.y = HEIGHT // 2
                enemies[0] = Enemy(200, 400, 150, 350, 2)
                enemies[1] = Enemy(600, 300, 550, 750, 3)

pgzrun.go()