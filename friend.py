from actor import *


class Friend(LoadActor):
    def __init__(self):
        super().__init__('codemao',  # model name
                         {"walk": "codemao_walk",  # animation name
                          'stand': "codemao_stand"},
                         (-600, -60, 0), 'friend', 30, 100)
#                       coordinates     node name ms   mh
        self.actor.setScale(0.7)
