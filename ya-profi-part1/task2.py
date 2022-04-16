n = int(input())
horizontal = []
vertical = []
for x in range(n-1):
    input_str = input()
    horizontal.append([int(i) for i in input_str])
for y in range(n):
    input_str = input()
    vertical.append([int(i) for i in input_str])

def move(mode = 0):
    global end_moving, path
    #step right
    if coords[1] != n-1 and vertical[coords[0]][coords[1]] == mode:
        end_moving = False
        if vertical[coords[0]][coords[1]] == 0:
            vertical[coords[0]][coords[1]] = 2
        else:
            vertical[coords[0]][coords[1]] = 1
        coords[1] += 1
        path += 'R'
    #step down
    elif coords[0] != n-1 and horizontal[coords[0]][coords[1]] == mode:
        end_moving = False
        if horizontal[coords[0]][coords[1]] == 0:
            horizontal[coords[0]][coords[1]] = 2
        else:
            horizontal[coords[0]][coords[1]] = 1
        coords[0] += 1
        path += 'D'
    #step up
    elif coords[0] != 0 and horizontal[coords[0]-1][coords[1]] == mode:
        end_moving = False
        if horizontal[coords[0]-1][coords[1]] == 0:
            horizontal[coords[0]-1][coords[1]] = 2
        else:
            horizontal[coords[0]-1][coords[1]] = 1
        coords[0] -= 1
        path += 'U'
    #step left
    elif coords[1] != 0 and vertical[coords[0]][coords[1]-1] == mode:
        end_moving = False
        if vertical[coords[0]][coords[1]-1] == 0:
            vertical[coords[0]][coords[1]-1] = 2
        else:
            vertical[coords[0]][coords[1]-1] = 1
        coords[1] -= 1
        path += 'L'

coords = [0,0]
path = ''
while True:
    end_moving = True
    move(0)
    if end_moving:
        move(2)
    
    if end_moving:
        break
print(len(path))
print(path)