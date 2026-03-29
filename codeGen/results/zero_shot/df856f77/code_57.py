n = int(input())  # Read the length of the array
arr = list(map(int, input().split()))  # Read the array elements

operations = 0
for i in range(1, n):
    while arr[i] <= arr[i-1]:
        arr[i] -= 1
        operations += 1

print(operations)
