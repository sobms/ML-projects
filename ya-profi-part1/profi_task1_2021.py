n = int(input())
consist_solution = False
k_list = [int(x) for x in input().split()]
k_list.sort()
for i in range(n):
    if i > 0 and (k_list[i-1] >= (n - i)):
        continue
    if k_list[i] >= (n - i):
        print(n - i)
        consist_solution = True
        break
if consist_solution == False:
    print(-1)
