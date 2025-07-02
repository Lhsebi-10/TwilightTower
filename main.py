import pyglet
from pyglet import shapes
from pyglet.gl.gl_compat import GL_NEAREST

import objects as obj
from pyglet.window import key

pyglet.image.Texture.default_min_filter = GL_NEAREST
pyglet.image.Texture.default_mag_filter =  GL_NEAREST


window = pyglet.window.Window(width=800, height=500)
MainPLayer = obj.Player(1, window.width / 2, 360)

MainPLayer.print_personalized_debuginfo("Player loaded!")


# pretend this is a real level system lol
totallyrealfloorcounter = pyglet.text.Label(f"Floor: 1 \n{MainPLayer.hasjumped}", font_name="arial", font_size=24,x=0,y=window.height,anchor_x="left",anchor_y="top")




@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.UP and not MainPLayer.jumping:
        MainPLayer.jumping = True
    elif symbol == key.H and not MainPLayer.show_hitboxes:
        MainPLayer.show_hitboxes = True
        print("showing hitboxes!")
    elif symbol == key.H and MainPLayer.show_hitboxes:
        MainPLayer.show_hitboxes = False
        print("not showing hitboxes!")
    else:
        MainPLayer.keys.add(symbol)
@window.event
def on_key_release(symbol, modifiers):
    if symbol == key.UP and MainPLayer.jumping:
        MainPLayer.jumping = False
    elif symbol in MainPLayer.keys:
        MainPLayer.keys.remove(symbol)




@window.event
def on_draw():
    window.clear()
    MainPLayer.show_player()
    MainPLayer.move()
    MainPLayer.apply_velocity(100)
    MainPLayer.animate_head()
    totallyrealfloorcounter.draw()


pyglet.app.run()