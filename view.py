from tkinter import *


root = Tk()

image_01 = PhotoImage(file = 'assets/floor.png')
image_02 = PhotoImage(file = 'assets/wall.png')
hero_down = PhotoImage(file = "assets/hero-down.png")
hero_up = PhotoImage(file = "assets/hero-up.png")
hero_right = PhotoImage(file = "assets/hero-right.png")
hero_left = PhotoImage(file = "assets/hero-left.png")
hero = PhotoImage(file = 'assets/hero-down.png') 
map_name = "map.txt"
canvas = Canvas(root, width = 700, height = 770, bg = 'white')
canvas.pack()

class Entity(object):
    def __init__(self, X = 35, Y = 35):
        self.X = X
        self.Y = Y
        self.costume = hero_down
        # self.image_entity = hero_down

    def move(self, dx, dy):
        canvas.move(self.image_entity, dx, dy)    
        
    
    def draw_hero(self):
           self.image_entity = canvas.create_image(self.X, self.Y, image = self.costume)


    def update_costume(self, costume):
        self.costume = costume
        canvas.itemconfigure(self.image_entity, image=self.costume)    


    def on_key_press(self, e):
        coords = canvas.coords(self.image_entity)
        # print(coords)
        if ( e.keysym == 'Up' ):
            if coords[1] > 35:
                self.move(0,-70)
                self.update_costume(hero_up)
                self.hero.update_costume(hero_up)
        elif( e.keysym == 'Down' ):
            if coords[1] < 666:
                self.move(0,70)
                self.update_costume(hero_down)
        elif( e.keysym == 'Right' ):
            if coords[0] < 665:
                self.move(70,0)
                self.costume = hero_right
                self.update_costume(hero_right)
        elif( e.keysym == 'Left' ):
            if coords[0] > 35:
                self.move(-70,0)
                self.costume = hero_left
                self.update_costume(hero_left)

class Hero(Entity):
    def __init__(self, X = 35, Y = 35):
        super().__init__(X, Y)


###   OPEN THE MAP FROM FILE   ###
def import_walls_to_list(file_name):
    try:
        with open(file_name, "r") as f:
            line_list = f.read().splitlines()
            return line_list
    except Exception:
        print("File read error")

###   OPEN THE MAP FROM LINES IN LINES   ###
def import_walls_to_list():
    line_list = [
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 1, 1, 0],
    [0, 1, 1, 1, 0, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 0]] 
    return line_list


def draw_tiles():
    wall_list = import_walls_to_list() #ADD map_name to input
    distance = 70
    for i, line in enumerate(wall_list):
       for j, value in enumerate(line):
            if str(value) == "0":
               image_floor = canvas.create_image(35+j*distance, 35+i*distance, image = image_01)
            elif str(value) == "1":
               image_floor = canvas.create_image(35+j*distance, 35+i*distance, image = image_02)

def chack_if_the_hero_goes_to_wall():
    for i, line in enumerate(wall_list):
           for j, value in enumerate(line):
               if i == 1:
                print(WALL)


    

draw_tiles()
hero = Entity()
hero.draw_hero()

root.bind("<KeyPress>", hero.on_key_press)

root.mainloop()

