from ursina import *
from scene_base import SceneBase


def setup(scene: SceneBase):
    """Menu Scene setup"""
    scene.name = "menu"
    
    # Kamerani sozlash
    camera.position = (0, 0, -3)
    camera.rotation = (0, 0, 0)
    mouse.locked = False
    
    # Menyu fon
    background = Entity(
        model='quad',
        scale=20,
        texture='sky_default',
        z=1,
        color=color.red
    )
    scene.add(background)
    
    # Sarlavha
    title = Text(
        text="XNS Engine Demo",
        x=0,
        y=0.3,
        origin=(0, 0),
        scale=4,
        color=color.white
    )
    scene.add(title)
    
    # O'yinni boshlash tugmasi
    def start_game():
        import scene_loader
        scene_loader.next_scene("world1")
    
    start_button = Button(
        text='O\'yinni Boshlash',
        color=color.green,
        scale=(0.3, 0.1),
        y=0,
        on_click=start_game
    )
    scene.add(start_button)
    
    # Chiqish tugmasi
    quit_button = Button(
        text='Chiqish',
        color=color.red,
        scale=(0.3, 0.1),
        y=-0.15,
        on_click=application.quit
    )
    scene.add(quit_button)


def handle_input(scene: SceneBase, key):
    """Menu input boshqaruvi - tugma bosilganda"""
    if key == 'escape':
        application.quit()
