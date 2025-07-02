import pyglet
from pyglet import shapes
from pyglet.window import key


class standardobject:
    def __init__(self, name, debugid):
        self.name = name
        self.debugid = debugid

    def print_debuginfo(self):
        print(f"Object {self.name}, with ID: {self.debugid} wants you to read this.")

    def print_personalized_debuginfo(self, caption):
        print(f"Object \"{self.name}\" with ID {self.debugid} wants you to know this: {caption} ")

# WHOAZ, ITZ A PLAYER
class Player(standardobject):
    def __init__(self, debugid, start_x, start_y):
        super().__init__("Player", debugid)
        self.x = start_x
        self.y = start_y
        self.physical_form = shapes.Rectangle(self.x, self.y, 25 * 1.5, 38 * 2.3, color=(255, 0, 0))
        self.keys = set()
        self.speed = 10
        self.gravity = -7
        # jumping shit
        self.jump_height = 200
        self.jump_progress = 0
        self.jumping = False
        self.hasjumped = False
        self.jump_speed = 10
        # M O T T I O N
        self.idleframe = pyglet.image.load("assets/p_idle1.png")
        self.idleframe.anchor_x = self.idleframe.width // 2 # this is to make the anchor of the image its center, making flipping look NORMAL
        self.walkframe1 = pyglet.image.load("assets/p_walk1.png")
        self.walkframe2 = pyglet.image.load("assets/p_walk2.png")
        self.currentframe = self.idleframe
        self.walkarray = [self.idleframe, self.walkframe1, self.idleframe, self.walkframe2]
        self.walkindex = 1
        self.sprite = pyglet.sprite.Sprite(img=self.currentframe,x=self.x,y=self.y)
        self.sprite.scale = 2.7
        self.show_hitboxes = False
        # attack stuff (how many more variables bro???)
        self.attacking = False

    def move(self):
        if key.LEFT in self.keys:
            self.x -= self.speed
        if key.RIGHT in self.keys:
            self.x += self.speed

    # the player knows where it is at all times. it knows this because it knows where it isnt.
    # the code knows where to draw the player, by knowing where it shoudnt
    def show_player(self):
        # this will ofc get expanded later, when we have a player and animation :p
        # these 2 lines are there to update the ""player sprites"" position, last one draws it
        self.physical_form.x = self.x - self.currentframe.width / 1.5
        self.physical_form.y = self.y + self.currentframe.height * 0.3
        self.sprite.x = self.x
        self.sprite.y = self.y
        if self.show_hitboxes:
            self.physical_form.draw()
        self.sprite.draw()
        playerlabel = pyglet.text.Label("Player", font_name="arial",font_size=18,x=self.x * 1.03, y=self.y + 120, anchor_x="center", anchor_y="center")
        playerlabel.draw()

    def apply_velocity(self, bottomline):
        # aplies gravity if the player isnt jumping and hasnt reached the bottom(-line)
        if self.jumping != True and self.y != bottomline:
            self.y += self.gravity
        elif self.jumping and self.hasjumped == False:
            #self.hasjumped = True
            if self.jump_progress < self.jump_height:
                self.y += self.jump_speed
                self.jump_progress += self.jump_speed
            else:
                self.jumping = False
                self.hasjumped = False
                self.jump_progress = 0
        #in case the player is under the bottom line (the ground), it readjusts itsself to the bottom line
        if self.y < bottomline:
            self.y = bottomline

    def attack(self): #swinging that thing around (ifykyk)
        if self.attacking:
            print("i dont wanna do thiiiiiiiiiiiiiiiiiis")


    # unused atm
    def animate_next_frame(self):
        # the index of walking gets increased
        self.walkindex + 1 % len(self.walkarray)
        # sets the frame to walkindex (so: idle -> walk1 -> idle, -> walk2)
        self.currentframe = self.walkarray[self.walkindex]


    # i'd rather shoot myself in the head than deal with one more line of clock_schedule, so here, have some fliping
    def animate_head(self):
        if key.LEFT in self.keys:
            self.sprite.scale_x = abs(self.sprite.scale_x)
        elif key.RIGHT in self.keys:
            self.sprite.scale_x = -abs(self.sprite.scale_x)


