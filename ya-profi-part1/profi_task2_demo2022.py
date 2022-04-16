from sys import stdout
a = -1
b = -1
for i in range(1, 1001):
    print('?', i)
    stdout.ﬂush()
    res = int(input())
    if res == 1 and a == -1:
        a = i
    elif res > 1 and a == -1:
        a = i
        b = i
        break
    elif res == 1 and a >= 0:
        if res % a != 0:
            b = i
            break
    elif res > 1:
            b = i - a
            break
    
print('!', a, b)
stdout.ﬂush()