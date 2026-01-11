from ursina import *
from scene_loader import next_scene, update as scene_update, handle_input as scene_handle_input

# Ursina ilovasini yaratish
app = Ursina(
    title='XNS Engine',
    borderless=False
)

# Oyna sozlamalari
window.fullscreen = False
window.exit_button.enabled = False
window.cog_button.enabled = False

# Boshlang'ich scene'ni yuklash
next_scene("menu")

def input(key):
    scene_handle_input(key)

def update():
    scene_update()

# Ilovani ishga tushirish
app.run()
