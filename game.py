import pgzrun, math, random
from pygame import Rect

# Config
WIDTH = 1024
HEIGHT = 600
TITLE = "Dungeon Phantom" 
TILE =  64
WALL_RECT = Rect(0, 0, 270, 225)

game_state = "MENU"
sound_enabled = True
music_enabled = True
music_playing = False
score = 0
score_timer = 0
intro_timer = 0

class GameObject:
    def __init__(self, prefix, x, y):
        self.grid_x = x
        self.grid_y = y
        self.prefix = prefix
        self.x = x*TILE
        self.y = y*TILE
        self.state = "idle"
        self.frame = 0
        self.timer = 0
        self.actor = Actor(f"{prefix}_idle_1", (self.x, self.y))
    def animate(self):
        self.timer += 1
        if self.timer > 10: self.timer, self.frame = 0, (self.frame + 1) % 2
        self.actor.image = f"{self.prefix}_{self.state}_{self.frame+1}"
    def smooth(self):
        tx, ty = self.grid_x*TILE, self.grid_y*TILE
        self.x += (tx-self.x)*0.2
        self.y += (ty-self.y)*0.2
        self.actor.pos = (self.x+TILE//2, self.y+TILE//2)
        self.state = "move" if math.hypot(tx-self.x, ty-self.y) > 2 else "idle"
    def draw(self): self.actor.draw()
    @property
    def hitbox(self): return self.actor.inflate(-self.actor.width*0.4, -self.actor.height*0.4)