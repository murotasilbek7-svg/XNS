from ursina import *

def norm_rgb(r, g, b, a=255):
    return color.rgba(r/255.0, g/255.0, b/255.0, a/255.0)


class SceneBase:
    """Asosiy Scene klassi"""
    
    def __init__(self):
        self.entities = []
        self.sky = None
        self.lights = []
        self.player = None
        self.is_active = False
        self.name = "unnamed"
    
    def update(self):
        """Har bir kadrda yangilash - Scene fayllarida to'ldirish kerak"""
        pass
    
    def handle_input(self, key):
        """Tugma kiritishlarini boshqarish"""
        if key == 'f11':
            window.fullscreen = not window.fullscreen
    
    def unload(self):
        """Scene yuklashni to'xtatish"""
        self.is_active = False
        
        if self.player:
            if self.player.enabled:
                self.player.enabled = False
            mouse.locked = False
            try:
                destroy(self.player)
            except:
                pass
            self.player = None
        
        if self.sky:
            try:
                self.sky.enabled = False
                if hasattr(Sky, 'instances') and self.sky in Sky.instances:
                    Sky.instances.remove(self.sky)
                destroy(self.sky)
            except:
                pass
            self.sky = None
        
        for light in self.lights:
            try:
                if hasattr(light, 'shadows') and light.shadows:
                    light.shadows = False
                destroy(light)
            except:
                pass
        self.lights.clear()
        
        for entity in self.entities:
            try:
                destroy(entity)
            except:
                pass
        self.entities.clear()
    
    def add(self, entity):
        """Entity qo'shish"""
        if entity:
            self.entities.append(entity)
