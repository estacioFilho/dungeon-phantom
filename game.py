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