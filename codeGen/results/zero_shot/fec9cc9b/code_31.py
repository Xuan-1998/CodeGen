# Read the input
n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = []
for _ in range(m):
    l, r = map(int, input().split())
    queries.append((l, r))
    
# Sort the array
arr.sort()
    
# Process each query
for l, r in queries:
    subsegment = arr[l-1:r]
    if is_ladder(subsegment):
        print("Yes")
    else:
        print("No")

def is_ladder(arr):
    decreasing = False
    increasing = False
    
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            decreasing = True
        elif arr[i] > arr[i-1]:
            increasing = True
            
        if decreasing and increasing:
            return False
            
    return True
