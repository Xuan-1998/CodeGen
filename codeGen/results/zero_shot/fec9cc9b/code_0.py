n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(m)]

def is_ladder(arr, l, r):
    # Check if the subsegment first doesn't decrease
    for i in range(l, r):
        if arr[i] < arr[i+1]:
            return False
    
    # Check if the subsegment then doesn't increase
    for i in range(l, r-1):
        if arr[i] > arr[i+1]:
            return False
    
    return True

for query in queries:
    l, r = query
    if is_ladder(arr, l-1, r):
        print("Yes")
    else:
        print("No")
