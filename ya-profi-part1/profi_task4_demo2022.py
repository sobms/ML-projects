n, m = input().split()
n = int(n)
m = int(m)
k_list = []
k_list = [int(i) for i in input().split()]
matrix = [[0 for i in range(n)] for i in range(n)]
for i in range(m):
    x, y = input().split()
    x = int(x)
    y = int(y)
    matrix[x][y] = 1
    matrix[y][x] = 1

common_friends = [0 for i in range(n)]

my_friends = []
new_people = []
for i in range(n - 1):
    if matrix[n - 1][i] == 1:
        my_friends.append(i)
    else:
        new_people.append(i)

for friend in my_friends:
    for i in range(n - 1):
        if matrix[friend][i]:
            common_friends[i] += 1


def search_friends():
    if (n - 1 == 0):
        return True
    while (True):
        count_new_friends = 0
        for i in range(len(new_people)):
            v = new_people[i]
            if matrix[n - 1][v] == 0 and common_friends[v] >= k_list[v]:
                matrix[n - 1][v] = 1
                matrix[v][n - 1] = 1
                count_new_friends += 1
                if v == 0:
                    return True
                for u in range(n - 1):
                    if matrix[i][u] == 1:
                        common_friends[u] += 1

        if not count_new_friends:
            return False


if search_friends():
    print('YES')
else:
    print('NO')