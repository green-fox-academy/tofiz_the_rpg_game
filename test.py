from tkinter import *
from random import randint


root = Tk()
# root.geometry('500x500+100+100')
# root.geometry('600x600')


image1 = PhotoImage(file = 'assets/floor.png')
image2 = PhotoImage(file = 'assets/wall.Png')
hero_down = PhotoImage(file = 'assets/hero-down.png')
hero_up = PhotoImage(file = 'assets/hero-up.png')
hero_left = PhotoImage(file = 'assets/hero-left.png')
hero_right = PhotoImage(file = 'assets/hero-right.png')
# skeleton = PhotoImage(file = 'assets/skeleton.png')
# boss = PhotoImage(file = 'assets/boss.png')

canvas = Canvas(root, width = 700, height = 770, bg = 'white')
canvas.pack()
image_floor = canvas.create_image(35, 35, image = image1)

def map_draw():
    file = open('map.txt', 'r')
    map_plan = file.readlines()
    file.close()
    a = 0
    for lines in map_plan:
        for elements in range(len(lines)-1):
            if lines[elements] == '1':
                image_floor = canvas.create_image(elements * 70 + 35, a + 35, image = image2)
            elif lines[elements] == '0':
                image_floor = canvas.create_image(elements * 70 + 35, a + 35, image = image1)
        a += 70
map_draw()

map = [[0, 0, 0, 1, 0, 1, 0, 0, 0, 0], 
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

def wall_or_floor(lines_index, element_index):  
    for i, lines in enumerate(map): # i=sor indexe, lines=érték
        for j, element in enumerate(lines):
            if i == lines_index and j == element_index and element == 0:
                print(str(element))
                return 0
            elif i == lines_index and j == element_index and element == 1:
                print(str(element))
                return 1
                
wall_or_floor(0, 3)


def cell_wall():
    print(get.cell(0,0))

class Entity(object):
    def __init__(self):
        self.x = 35
        self.y = 35
        self.costume = hero_down

    def entity_draw(self):
        self.image_entity = canvas.create_image(self.x , self.y, image = self.costume)
       
    def move(self, dx, dy):
        canvas.move(self.image_entity, dx, dy )

    def update_costume(self, costume):
        self.costume = costume
        canvas.itemconfigure(self.image_entity, image=self.costume)

    def on_key_press(self, e):
        coords = canvas.coords(self.image_entity)
        print(coords)
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
    def __init__(self):
        pass

hero = Entity()
hero.entity_draw()


root.bind("<KeyPress>", hero.on_key_press)

root.mainloop()