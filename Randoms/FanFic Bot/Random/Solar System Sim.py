from ursina import *
from panda3d.core import Camera as PandaCamera

app = Ursina()
window.fps_counter.enabled = True

camera.perspective = True
camera.fov = 35

cube = Entity(model='cube', color=color.white, scale=(2,6,2), texture="water.jpg")

for cube in cube:
    cube.rotation_y += time.dt * 5

app.run()
