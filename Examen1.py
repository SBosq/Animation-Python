import pyglet
from pyglet import shapes

width = 500
height = 500
title = "Circulos Examen"
window = pyglet.window.Window(width, height, title)
batch = pyglet.graphics.Batch()
circle_x = 300
circle_y = 300
size_circle = 100
circle1 = shapes.Circle(circle_x, circle_y, size_circle, color=(1, 120, 27), batch=batch)
circle2 = shapes.Circle(circle_x - 150, circle_y - 150, size_circle - 20, color=(99, 99, 99), batch=batch)
circle2.opacity = 200


@window.event
def on_draw():
    window.clear()
    batch.draw()


pyglet.app.run()
