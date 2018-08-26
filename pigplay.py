'''
Play on pyglet
'''

import pyglet
from pyglet import app
from pyglet.window import key
from pyglet.window import mouse


pyglet.options['debug_gl'] = False

wind = pyglet.window.Window()



'''
Keyboard events have two parameters: the virtual key symbol that was pressed,
 and a bitwise combination of any modifiers that are present
  (for example, the CTRL and SHIFT keys).

The key symbols are defined in pyglet.window.key:


'''

@wind.event
def on_key_press(symbol, modigiers):
    if symbol == key.A:
        print('A key was pressed')
    elif symbol == key.LEFT:
        print('The left arrow key was pressed')
    elif symbol == key.ENTER:
        print('The enter key was pressed')


'''
The x and y parameters give the position of the mouse when the button was pressed, 
relative to the lower-left corner of the window.

There are more than 20 event types that you can handle on a window. 

The easiest way to find the event name and parameters you need is to add the following line to your program:

window.push_handlers(pyglet.window.event.WindowEventLogger())

This will cause all events received on the window to be printed to the console.

An example program using keyboard and mouse events is in examples/programming_guide/events.py

'''

@wind.event
def on_mouse_press(x,y, button, modifiers):
    if button == mouse.LEFT:
        print('Left button pressed')
    elif button == mouse.RIGHT:
        print('Right button pressed')



@wind.event
def on_draw():
    wind.clear()


wind.push_handlers(pyglet.window.event.WindowEventLogger())


app.run()