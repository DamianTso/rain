'''
Play on pyglet
'''

import pyglet
from pyglet import app


pyglet.options['debug_gl'] = False

wind = pyglet.window.Window()


@wind.event
def on_key_press(symbol, modigiers):
    if symbol == key.A:
        print('A key was pressed')
    elif symbol == key.LEFT:
        print('The left arrow key was pressed')
    elif symbol == key.ENTER:
        print('The enter key was pressed')



@wind.event
def on_draw():
    wind.clear()






app.run()