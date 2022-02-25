#pandas3d game / final

#Class -> OOP Coding
#Like Data Definitions in Dr. Racket

#import libraries
from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from direct.gui.DirectGui import *
from player import *
from friend import *
from enemy import *

#Create a base class
class Configure(ShowBase):
    def __init__(self): #Create initiation function
        super().__init__() #initiate ShowBase
        self.font=loader.loadFont("font.ttc")
        self.setup()
    def setup(self):
        self.window_properties(1400, 1000) #Sets the width and height of the window
        #creates a window popup (dialog)
        self.start_dialog = self.create_dialog(frame_size=(-1.41, 1.41, -1.01, 1.01), #sets size of window
                           pos=(0,0,0), #sets location of window
                           color=(1,1,1,1), #sets color of window
                           picture="start.png") #sets background color of window
        self.create_button(pos=(0,0,-0.8), #sets position (only cares about x and y axes)
                           text="Start Game", #sets text of button
                           parent=self.start_dialog, #sets what the button operates on (parent)
                           command=self.start, #sets what happens when button is clicked
                           scale=0.15, #sets the size (scaling) of the button
                           fg=(255/255, 220/255, 99/255, 1), #sets the text color of the button
                           frameColor=(147/255, 88/255, 51/255, 1)) #sets the background color of the button

    def window_properties(self, width, height):
        self.window = WindowProperties()
        self.window.setSize(width, height)
        self.win.requestProperties(self.window)
        #adding window properties to window
    def create_dialog(self, frame_size, pos, color, picture):
        return DirectDialog(frameSize=frame_size,
                     frameColor=color,
                     pos=pos,
                     frameTexture=picture)
        #function to create window popup
    def create_button (self, text, parent, command, scale, pos, fg, frameColor):
        DirectButton(text=text,
                     parent=parent,
                     command=command,
                     scale=scale,
                     pos=pos,
                     text_font=self.font,
                     text_fg=fg,
                     frameColor=frameColor)
    def start(self): #command function for button
        self.start_dialog.hide()
        self.load_model("FieldForest")
        #changes the rotational perspective of .egg file
        base.cam.setHpr(-90, -4, 0)
        #changes the position of .egg file
        base.cam.setPos(-1000, -100, 100)
        #create capsule collision objects:
        self.create_fence(580, 350, 0, 580, -350, 0, 5)
        self.create_fence(-580, -350, 0, 580, -350, 0, 5)
        self.create_fence(-580, -350, 0, -580, -150, 0, 5)
        self.create_fence(-580, -40, 0, -580, 350, 0, 5)
        self.create_fence(-580, 350, 0, 580, 350, 0, 5)
        base.disableMouse()
        self.player = Player()
        self.friend = Friend()
        self.woodmen = EnemyWoodman()
        self.needle = EnemyNeedle()

        self.key_state = {'up':False, 'left':False, 'right': False} 

        self.key_event()
        
    #how to load .egg files
    def load_model(self, model):
        self.model = loader.loadModel(model)
        self.model.reparentTo(render)

    #create a collision object
    def create_fence(self, ax, ay, az, bx, by, bz, r):
        fence_solid = CollisionCapsule(ax, ay, az, bx, by, bz, r)
        #create a capsule with pos (ax, ay, az) (bx, by, bz) and radius r
        fence_node = CollisionNode('fence')
        #create a collision node
        fence_node.addSolid(fence_solid)
        #add capsule to node
        render.attachNewNode(fence_node)
        #render node
    
    def change_key_state(self, direction, key_state):
        self.key_state[direction] = key_state
    
    def key_event(self):
        self.accept('w', self.change_key_state, ['up', True])
        self.accept('w-up', self.change_key_state, ['up', False])
        self.accept('d', self.change_key_state, ['right', True])
        self.accept('d-up', self.change_key_state, ['right', False])
        self.accept('a', self.change_key_state, ['left', True])
        self.accept('a-up', self.change_key_state, ['left', False])
        
    def update(self, task):
        dt = globalClock.getDt() #get the run duration
        self.player.aduan_move(self.key, dt)

        return task.cont



#Allows the game to start running 
start_game = Configure()
start_game.run()


