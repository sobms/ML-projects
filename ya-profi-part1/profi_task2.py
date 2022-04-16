from sys import stdout
n, u, v = input().split()
n = int(n)
u = len(u)
v = len(v)
count = 0
if (v>u):
    u,v = v,u
place = 1
while True:
    if (place+1000 <= n):
        print('?', place, place+1000)
        stdout.ﬂush()
        count += int(input())
        
        if (place + 1000 + u) < n:
            print('?', place+1000-u, place+1000+u)
            stdout.ﬂush()
            count += int(input())
            place += 1000+u
        else:
            print('?', place+1000-u, n)
            stdout.ﬂush()
            count += int(input())
            break
    else:
        print('?', place, n)
        stdout.ﬂush()
        count += int(input())
        break
print('!', count)
stdout.ﬂush()