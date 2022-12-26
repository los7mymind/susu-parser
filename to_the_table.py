import pandas as pd

with open("result.txt", 'r') as file:
    arr = file.read()
    arr = arr[1:-1].split(', ')
    arr1 = []
    for i in range(len(arr)):
        if '/' in arr[i]:
            arr1.append(arr[i])

    arr = arr1
    for i in range(len(arr1)):
        arr[i] = [arr[i][1:-1], arr[i][arr[i].index('/') + 1:-1]]

    arr = sorted(arr, key=lambda x: x[1])

buildings = []

temp = []
new_arr = []
for i in range(len(arr) - 1):
    if arr[i][1] == arr[i + 1][1]:
        temp.append(arr[i][0])
    else:
        temp.append(arr[i][0])
        new_arr.append(temp)
        buildings.append(f'Корпус -- {arr[i][1]}')
        temp = []

max_len = 0
for i in new_arr:
    max_len = max(max_len, len(i))

for i in range(len(new_arr)):
    for j in range(max_len - len(new_arr[i])):
        new_arr[i] += '-'

df = pd.DataFrame(new_arr, index=buildings)
df = df.transpose()
df.to_csv('Audiences.csv')
