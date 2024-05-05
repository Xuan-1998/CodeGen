code
n = int(input())
arr = list(map(int, input().split()))
last_index_reachable = False

current_index = 0
while current_index < n - 1:
    jump_length = arr[current_index]
    if current_index + jump_length >= n - 1:
        last_index_reachable = True
        break
    current_index += 1

print(last_index_reachable)
