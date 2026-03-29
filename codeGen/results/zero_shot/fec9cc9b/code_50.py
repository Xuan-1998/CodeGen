import sys

n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = []

for _ in range(m):
    l, r = map(int, input().split())
    queries.append((l-1, r))

def is_ladder(arr, left, right):
    decrease = False
    increase = False
    
    for i in range(left, right+1):
        if arr[i] < arr[i-1]:
            increase = True
        elif arr[i] > arr[i-1]:
            decrease = True
        
    return not (decrease and increase)

for query in queries:
    left, right = query
    print("Yes" if is_ladder(arr, left, right) else "No")
