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

class Character(GameObject):
    def try_move(self, dx, dy, blockers):
        nx, ny = self.grid_x+dx, self.grid_y+dy
        if not (0 <= nx < WIDTH//TILE and 0 <= ny < HEIGHT//TILE): return False
        if WALL_RECT.collidepoint(nx*TILE + TILE//2, ny*TILE + TILE//2): return False
        if any(b.grid_x==nx and b.grid_y==ny for b in blockers): return False
        self.grid_x, self.grid_y = nx, ny
        return True

class Enemy(Character):
    def __init__(self, x, y):
        super().__init__("enemy", x, y)
        self.ai_timer = 0
    def ai(self, target, others):
        self.ai_timer += 1
        if self.ai_timer < 60: return
        self.ai_timer = 0
        dx = (1 if target.grid_x>self.grid_x else -1 if target.grid_x<self.grid_x else 0) if random.random()<0.7 else random.choice([1,-1,0,0])
        dy = (1 if target.grid_y>self.grid_y else -1 if target.grid_y<self.grid_y else 0) if random.random()<0.7 else random.choice([1,-1,0,0])
        if dx and dy:
            if random.random()<0.5: dx=0 
            else: dy=0
        if self.try_move(dx, dy, [target]+others) and sound_enabled:
            try: sounds.enemy_move.play()
            except: pass

hero = Character("hero", 10, 7)
enemies = []
def spawn_enemies():
    enemies.clear()
    for _ in range(3): enemies.append(Enemy(random.randint(4,10), random.randint(4,8)))
def start_game():
    global game_state, score, score_timer, intro_timer
    spawn_enemies(); hero.grid_x, hero.grid_y = 10, 7; hero.x, hero.y = 10*TILE, 7*TILE
    score, score_timer, intro_timer, game_state = 0, 0, 180, "PLAYING"
spawn_enemies()

btn_start, btn_sound, btn_music, btn_exit = [Rect(WIDTH//2-100, 180+i*60, 200, 45) for i in range(4)]