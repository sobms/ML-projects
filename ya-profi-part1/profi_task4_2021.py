from random import choice

k = int(input())
coords = []
search_path = ''
#Rad = 1
#while len(search_path) < 1000*k:
#        search_path += 'U' * Rad + 'R' * Rad + 'D' * 2*Rad + 'L' * 2*Rad + 'U' * 2*Rad + 'R' * Rad + 'D' * Rad
#        Rad+=1   
options = [ 'U', 'R', 'D', 'L' ]
for i in range(1000*k):
    search_path += choice(options)

for i in range(100):
    coords.append(tuple(int(x) for x in input().split()))

for x, y in coords:
    path = ''
    if (x > 0):
        path += 'R' * abs(x)
    else:
        path += 'L' * abs(x)
    if (y > 0):
        path += 'U' * abs(y)
    else:
        path += 'D' * abs(y)
    path = path[:1000*k]
    random_path_len = 1000*k - len(path)
    print((path+search_path[:random_path_len]))
