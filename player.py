from actor import *

class Player(LoadActor):
    def __init__(self):
        super().__init__('aduan', #model name
                        {"walk":"aduan_walk", #animation name
                        'stand':"aduan_stand"},
                        (-600, -60, 0), 'player', 30, 100)
#                       coordinates     node name ms   mh
        self.actor.setScale(4.5)
        self.acceleration = 100

    def aduan_move(self, keys, dt):
        LoadActor.move(self, dt) 
        self.walking = False

        if keys['up']:
            self.velocity.addY(self.acceleration*dt) #accelerates to dt ratio
            self.walking = True
        
        if keys['left']:
            self.velocity.setH(self.actor.getH() + 1)  # moves left 1
            self.walking = True

        if keys['right']:
            self.velocity.setH(self.actor.getH() - 1)  # moves right 1
            self.walking = True

        if self.walking:
            walk_control =s
