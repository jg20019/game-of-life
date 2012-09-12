from time import sleep
from copy import deepcopy
from os import system

LIVE = True
DEAD = False
WIDTH, HEIGHT = SIZE = (5,5)

def make_world():
    w = {}
    for i in range(WIDTH):
        for j in range(HEIGHT):
            w[(i,j)] = DEAD
    w[(1,2)] = LIVE
    w[(2,2)] = LIVE
    w[(3,2)] = LIVE

    return w

def print_world(world):
    l = []

    for i in range(WIDTH):
        line = []

        for j in range(HEIGHT):
            if world[(i,j)]:
                line.append('#')
            else:
                line.append(' ')

        l.append(''.join(line))
    print('\n'.join(l))


def check_live(cell,world):
    return cell in world and world[cell]

def get_neighbors(cell):
    x,y = cell
    for i in [-1,1]:
        yield (x+i,y)
        yield (x,y+i)
        yield (x+i,y+i)
        yield (x+i,y-i)

def get_live_neighbors(cell, world):
    return [c for c in get_neighbors(cell) if check_live(cell,world)]

def count_live_neighbors(cell, world):
    x,y = cell
    liveCount = 0
    return sum([1 for cell in get_neighbors(cell) if check_live(cell,world)])

def handle_live_cell(cell,world,ref):
    c = count_live_neighbors(cell,ref)

    if c == 2 or c == 3:
        world[cell] = LIVE
    else:
        world[cell] = DEAD

def handle_dead_cell(cell,world,ref):
    c = count_live_neighbors(cell,ref)
    if c == 3:
        world[cell] = LIVE

handle_cell = {LIVE : handle_live_cell, DEAD : handle_dead_cell}

def main():
    world = make_world()
    
    while True:
        print_world(world)

        refWorld = deepcopy(world)
        for cell in refWorld:
            handle_cell[refWorld[cell]](cell,world,refWorld)
        sleep(1)
        system('cls')

if __name__ == '__main__':
    main()
