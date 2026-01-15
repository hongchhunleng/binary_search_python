def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i # reaturn index
    return -1 # not found

numbers = [ 10, 20, 30, 40, 50]
target = int(input(":"))

print(linear_search(numbers, target))