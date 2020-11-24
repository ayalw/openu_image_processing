import sys


def find_smallest(arr):
    smallest = sys.maxsize
    for item in arr:
        if item < smallest:
            smallest = item
    return smallest


def k_smallest_1(arr, k):
    temp_arr = []
    for j in range(k):
        min_item = min(arr)
        for l in range(len(arr)):
            if arr[l] == min_item:
                arr[l] = sys.maxsize
        temp_arr.append(min_item)
    return temp_arr


def k_smallest(arr, k):
    temp_arr = []
    for j in range(k):
        temp_arr.append(sys.maxsize)
    for j in range(len(arr)):
        for l in range(k):
            if arr[j] < temp_arr[l]:
                temp_arr[l] = arr[j]
                break
    return temp_arr


print('hello')
input_arr = [10, 2, 30, 40, 5]
smallest_item = find_smallest(input_arr)
print('smallest='+str(smallest_item))
input_k = 3
result = k_smallest_1(input_arr, input_k)
res_str = ''
for i in result:
    res_str += '[' + str(i) + ']'
print(res_str)
