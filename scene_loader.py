from scene_base import SceneBase
import importlib
import os

_scenes = {}
_current_scene = None
_scenes_loaded = False


def _auto_register_scenes():
    """Scenes papkasidan barcha Scene'larni avtomatik topish"""
    global _scenes_loaded, _scenes
    
    if _scenes_loaded:
        return
    
    scenes_dir = os.path.join(os.path.dirname(__file__), 'scanes')
    
    if os.path.exists(scenes_dir):
        for file in os.listdir(scenes_dir):
            if file.endswith('.py') and file != '__init__.py':
                scene_name = file[:-3]
                module_name = f'scanes.{scene_name}'
                _scenes[scene_name] = module_name
                print(f"✓ Scene yuklandi: {scene_name}")
    
    _scenes_loaded = True


def next_scene(name: str):
    """Belgilangan Scene'ga o'tish"""
    global _current_scene, _scenes_loaded
    
    if not _scenes_loaded:
        _auto_register_scenes()
    
    if name not in _scenes:
        print(f"Xato: '{name}' Scene topilmadi!")
        return None
    
    if _current_scene:
        _current_scene.unload()
    
    scene = SceneBase()
    _current_scene = scene
    
    try:
        module = importlib.import_module(_scenes[name])
        
        if hasattr(module, 'setup'):
            module.setup(scene)
            scene.is_active = True
        else:
            print(f"Xato: '{name}' Scene'da setup() funksiyasi topilmadi!")
            return None
    except Exception as e:
        print(f"Xato: '{name}' Scene yuklashda xatolik: {e}")
        import traceback
        traceback.print_exc()
        return None
    
    return scene


def update():
    """Hozirgi Scene ni yangilash"""
    global _current_scene
    
    if _current_scene and _current_scene.is_active:
        _current_scene.update()
        
        scene_name = None
        for name, module_name in _scenes.items():
            if _current_scene.name == name:
                scene_name = module_name
                break
        
        if scene_name:
            try:
                module = importlib.import_module(scene_name)
                if hasattr(module, 'update'):
                    module.update(_current_scene)
            except:
                pass


def handle_input(key):
    """Hozirgi Scene input boshqaruvi"""
    global _current_scene
    
    if _current_scene and _current_scene.is_active:
        _current_scene.handle_input(key)
        
        scene_name = None
        for name, module_name in _scenes.items():
            if _current_scene.name == name:
                scene_name = module_name
                break
        
        if scene_name:
            try:
                module = importlib.import_module(scene_name)
                if hasattr(module, 'handle_input'):
                    module.handle_input(_current_scene, key)
            except:
                pass
