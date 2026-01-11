from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from scene_base import SceneBase, norm_rgb


def setup(scene: SceneBase):
    """World1 Scene setup"""
    scene.name = "world1"
    mouse.locked = True
    
    # Sky
    sky = Sky()
    scene.sky = sky
    map_layout = [
        "w...wwwwwwwwwwwwwwww",
        "w..................w",
        "wwwwwwwwwwwwwww... w",
        "w..................w",
        "w..wwwwwwwwwwwwwwwww",
        "w..................w",
        "wwwwwwwwwwwwww.....w",
        "w..................w",
        "w....wwwwwwwwwwwwwww",
        "w..................w",
        "wwwwwwwwwwwwwww.....",
    ]

    block_scale = 9 # Xohlagan masshtabingizni shu yerga kiriting
    labirint = False
    if labirint:
        for z, row in enumerate(map_layout):
            for x, char in enumerate(row):
                if char == "w":
                    Entity(
                        model='cube',
                        collider='box',
                        position=(x * block_scale, block_scale / 2, z * block_scale),
                        scale=(block_scale, block_scale, block_scale),
                        texture='brick',
                        color=color.gray
                    )
    
    # Yer (Ground)
    ground = Entity(
        model='plane',
        scale=(500, 1, 120),
        position=(0, 0, 29),
        color=color.white,
        collider='box',
        texture='grass'
    )
    terrain = Entity(
    model='models/rock/rock.obj',
    texture='models/rock/rock_face_03.png',
    scale=(3,3,3),
    collider='mesh'
    )


    # Qo'shimcha yuzalar
    wall = Entity(
        model='plane',
        scale=(50, 1, 70),
        position=(-25, 25, 0),
        color=color.white,
        collider='box',
        texture='brick',
        rotation=(0, 0, 90)
    )
    wall1 = Entity(
        model='plane',
        scale=(50, 1, 70),
        position=(25, 25, 0),
        color=color.white,
        collider='box',
        texture='brick',
        rotation=(0, 0, 270)
    )
    
    wall2 = Entity(
        model='plane',
        scale=(50, 1, 70),
        position=(-1, 25, -30),
        color=color.white,
        collider='box',
        texture='brick',
        rotation=(0, -90, 90)
    )
    

    # Quyosh (Sun) - Yoritish
    sun = DirectionalLight(
        shadows=False,
        color=norm_rgb(255, 250, 240),
        intensity=1.5
    )
    sun.look_at(Vec3(-1, -2, -1))
    scene.lights.append(sun)
    
    # Ambient Light - Atrof muhit yoritishi
    ambient = AmbientLight(
        color=norm_rgb(60, 60, 70, 255)
    )
    scene.lights.append(ambient)
    
    # UI - Player pozitsiyasini ko'rsatish
    position_text = Text(
        text="Position: X:0 Y:2 Z:-5",
        x=-0.50,
        y=0.45,
        scale=2,
        color=color.yellow
    )
    scene.add(position_text)
    scene.position_text = position_text
    
    # Player yaratish
    player_controller = FirstPersonController(
        position=(0, 2, -5),
        speed=8,
        enabled=True,
        jump_height=6,
        jump_duration=1,
        gravity=2,
        collider='box'
    )
    player_controller.base_speed = 16
    player_controller.run_speed = 26
    player_controller.stamina = 1.0
    player_controller.is_running = False
    scene.player = player_controller
    mouse.locked = True
    
    # Scene obyektlari - Kub
    cube = Entity(
        model='cube',
        scale=(2, 2, 2),
        position=(5, 1, 5),
        color=color.white,
        collider='box',
        texture='Texture/Cube_2/texture.png',
        rotation=(0, 0, 0)
    )
    cube.cast_shadows = True
    scene.add(cube) 
    scene.cube = cube


def update(scene: SceneBase):
    """World1 update - har bir kadrda yangilash"""
    
    # Player yangilash - stamina va tezlik boshqaruvi
    if scene.player and scene.player.enabled:
        is_running = held_keys['left shift'] or held_keys['right shift']
        
        if is_running and scene.player.stamina > 0.05:
            scene.player.speed = scene.player.run_speed
            scene.player.stamina -= time.dt * 0.2
            scene.player.is_running = True
        else:
            scene.player.speed = scene.player.base_speed
            scene.player.is_running = False
        
        if not scene.player.is_running:
            scene.player.stamina = min(1.0, scene.player.stamina + time.dt * 0.15)
        if scene.player.position.y < -50:
            # O'yinchini xavfsiz nuqtaga (masalan, Y=1) qaytarish
            scene.player.position = (0, 1, 0)
    # UI yangilash - Player pozitsiyasini ko'rsatish
    if hasattr(scene, 'position_text') and scene.position_text and scene.player and scene.player.enabled:
        pos = scene.player.position
        scene.position_text.text = f"Pos: X:{round(pos.x, 2)} Y:{round(pos.y, 2)} Z:{round(pos.z, 2)} | Scene: {scene.name} | speed: {scene.player.speed}"
    if hasattr(scene, 'cube'):
        scene.cube.rotation_y += time.dt * 50  # Kubni aylantirish
        scene.cube.rotation_x += time.dt * 50

def handle_input(scene: SceneBase, key):
    """World1 input boshqaruvi - tugma bosilganda"""
    if key == 'escape':
        import scene_loader
        scene_loader.next_scene("menu")

def handle_input(scene: SceneBase, key):
    """World1 input boshqaruvi - tugma bosilganda"""
    # ... Boshqa tugmalarni boshqarish (escape kabi) ...
    if key == 'escape':
        import scene_loader
        scene_loader.next_scene("menu")
    if key == 'f':
        # 1. HOLAT: Agar Player faol bo'lsa, EditorCamera'ga o'tish
        if scene.player and scene.player.enabled:
            # Player'ni o'chirish va sichqonchani chiqarish
            scene.player.enabled = False
            mouse.locked = False
            
            # EditorCamera'ni sozlash / yaratish
            if hasattr(scene, 'editor_cam') and scene.editor_cam:
                editor_cam = scene.editor_cam
            else:
                editor_cam = EditorCamera(enabled=False, speed=30) # Dastlab o'chirilgan holatda yaratamiz
                scene.editor_cam = editor_cam

            # Kamerani Player pozitsiyasiga o'tkazish
            editor_cam.position = scene.player.position
            
            # 💡 MUHIM QADAM: Aylanish (Pivot) muammosini hal qilish
            # Kamerani to'g'ri burilish nuqtasiga qaytarish uchun
            editor_cam.rotation = scene.player.rotation # Playerning burilishini olish (yangi boshlang'ich yo'nalish)
            
            # EditorCamera'ning default aylanish fokusini Player pozitsiyasiga yaqinlashtirish
            # Ba'zi EditorCamera versiyalarida bu aylanish markazini tiklaydi.
            camera.look_at(editor_cam.position + editor_cam.forward * 0.01) # Juda yaqin nuqtaga fokuslash

            editor_cam.enabled = True
            print("EditorCamera yoqildi. Qaytish uchun yana 'F' tugmasini bosing.")

        # 2. HOLAT: Agar EditorCamera faol bo'lsa, Player'ga qaytish
        elif hasattr(scene, 'editor_cam') and scene.editor_cam and scene.editor_cam.enabled:
            # EditorCamera'ni o'chirish
            scene.editor_cam.enabled = False
            
            # FirstPersonController'ni yoqish
            scene.player.enabled = True
            mouse.locked = True
            
            # O'yinchining pozitsiyasini EditorCamera'ning joriy pozitsiyasiga yangilash
            scene.player.position = scene.editor_cam.position 
            scene.player.rotation = scene.editor_cam.rotation # Burilishni ham qaytarish
            
            print("FirstPersonController yoqildi.")