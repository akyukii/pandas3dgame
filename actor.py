from direct.actor.Actor import Actor
from panda3d.core import *

class LoadActor(Actor):
    def __init__ (self, modelName, animsName, pos, actorname, max_speed, max_health):
        super().__init__()
        #create actor with (Name of Actor, Route of movement)
        self.actor = Actor(modelName, animsName)
        #add actor to list render
        self.actor.reparentTo(render)
        #set position of actor
        self.actor.setPos(pos)
        #create a spherical collider object
        sphere = CollisionSphere(0, 0, 0, 5)
        collider_node = CollisionNode(actorname)
        collider_node.addSolid(capsule)
        self.collider = self.actor.attachNewNode(collider_node)
        self.max_speed = max_speed # the max speed changes for every actor, therefore it changes
        self.velocity = Vec3(0,0,0) #velocity is expressed through a vector
        self.NeAcc = 500
        self.walking = False
        self.max_health = max_health #max health
        self.health = max_health #current health

    def move(self, dt):
        speed = self.velocity.length()
        if speed > self.max_speed:
            self.velocity.normalize() # normalize? 归一化
            self.velocity *= self.max_speed #multiply by max speed
            speed = self.max_speed
        if not self.walking: #if actor is not walking
            NeSpeed = self.NeAcc * dt
            if NeSpeed > speed: #if opposite speed is larger than current speed
                self.velocity = Vec3(0,0,0) #set current speed to be 0
            else:
                slow_speed = -self.velocity #slowly step the current speed down towards the negative speed
                slow_speed.normalize() #normalize the slow speed
                slow_speed *= NeSpeed #multiply by opposite speed
                self.velocity += slow_speed #this is slowing down the current speed 
        self.actor.setY(self.actor, -(self.velocity * dt).length()) #move the actor relative to themselves, slowing down

    def count_health(self, health_change):
        self.health += health_change
        if self.health > self.max_health: #health can only be maximum max health
            self.health = self.max_health #set health to be max health
    
    def clean_up(self):
        if self.collider is not None:
            base.cTrave.removeCollider(self.collider) #remove itself, cleans up the scene
            self.collider = None
        if self.actor is not None:
            self.actor.cleanup() #cleans up actor data
            self.actor.removeNode() #removes the actor from the scene
            self.actor = None #the actor is gone
    



