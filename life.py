from time import sleep
from os import system

LIVE = 1
DEAD = 0

def make_world():
    w = {}
    for i in range(5):
        for j in range(5):
            w[(i,j)] = DEAD
    w[(2,1)] = LIVE
    w[(2,2)] = LIVE
    w[(2,3)] = LIVE

    return w

def print_world(world):
    l = []
    for i in range(5):
        for j in range(5):
            j = []
            if world[(i,j)] == LIVE:
                j.append('#')
            else:
                j.append(' ')
        l.append(''.join(j))
    print '\n'.join(l)

def count_live_neighbors():
    pass

def handle_live_cell(cell, world):
    c = count_live_neighbors(cell, world)
    if c < 2:
        world[cell] = DEAD
    elif c == 2 or c == 3:
        world[cell] = LIVE
    elif c > 3:
        world[cell] == DEAD

def handle_dead_cell(cell,world):
    c = count_live_neighbors(cell,world)
    if c == 3:
        world[cell] = LIVE

handle_cell = {LIVE : handle_live_cell, DEAD : handle_dead_cell}

world = make_world()
while True:
    #for cell in world:
    #handle_cell[world[cell]](cell,world)
    print_world(world)
    sleep(1)
