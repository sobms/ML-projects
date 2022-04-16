import numpy as np
#ввод данных
n = int(input())
max_elem = 0
arr = np.zeros(n, dtype=int)
for i in range(0, n):
  arr[i] = int(input())
  if (arr[i]>max_elem):
    max_elem = int(arr[i])
#сортировка
arr_c = np.zeros(max_elem+1, dtype=int)
for i in range(0, len(arr)):
  arr_c[arr[i]] += 1

for i in range(1, len(arr_c)):
  arr_c[i] = arr_c[i-1] + arr_c[i]

arr_sort = np.empty(arr.shape)
for i in range(0, len(arr)):
  arr_sort[arr_c[arr[i]]-1] = arr[i]
  arr_c[arr[i]] -= 1
#поиск числа рыцарей
consist_solution = False
for i in range(0, len(arr_sort)):
  knights = len(arr_sort) - i
  if i > 0 and arr_sort[i-1] >= knights:
    continue
  if knights <= arr_sort[i]:
    consist_solution = True
    print(knights)
if consist_solution == False:
  print(-1) 