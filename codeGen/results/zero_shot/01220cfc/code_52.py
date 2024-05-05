code
n = int(input())
arr = list(map(int, input().split()))
last_index_reachable = 0

for i in range(n):
    if i > last_index_reachable:  # If we can't reach this index, break
        print(False)
        break
    last_index_reachable = max(last_index_reachable, arr[i] + i)

if last_index_reachable >= n - 1:
    print(True)
else:
    print(False)
