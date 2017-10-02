class Entity(object):
    def __init__(self, X = 35, Y = 35):
        self.X = X
        self.Y = Y


    def draw(self, entity_image):
        self.entity_image = entity_image


    
class Hero(Entity):
    def __init__(self, X = 35, Y = 35):
        super().__init__(X, Y)
