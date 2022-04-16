n = int(input())
matr = []
for i in range(0, n):
    matr.append([int(i) for i in list(input().split())])
    
group1 = [0]
group2 = []
for i in range(1, n):
    if matr[0][i]:
        group1.append(i)
    else:
        group2.append(i)
group1 = set(group1)
group2 = set(group2)

for i in range(0, 4):
    for v in range(0, n):
            if v in group1:
                count_neighbors = 0
                for neighbour in group1:
                    if matr[v][neighbour]:
                        count_neighbors += 1
                if count_neighbors >= n * 0.25:
                    group1.remove(v)
                    group2.add(v)
            if v in group2:
                count_neighbors = 0
                for neighbour in group2:
                    if matr[v][neighbour]:
                        count_neighbors += 1
                if count_neighbors >= n * 0.25:
                    group2.remove(v)
                    group1.add(v)
for i in range(0, n):
    if i in group1:
        print(i+1, 1)
    else:
        print(i+1, 2)