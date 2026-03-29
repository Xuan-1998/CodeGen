import sys

def can_reach_last(arr):
    max_reach = 0
    for i in range(len(arr)):
        if i <= max_reach + arr[i]:
            max_reach = i + arr[i]
    return max_reach >= len(arr) - 1

arr = [int(x) for x in sys.stdin.readline().split()]
print(can_reach_last(arr))
