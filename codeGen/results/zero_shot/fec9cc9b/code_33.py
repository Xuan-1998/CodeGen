# Receive the input
n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = []

for _ in range(m):
    l, r = map(int, input().split())
    queries.append((l-1, r))

# Function to check if a subsegment is a ladder
def is_ladder(arr, l, r):
    increasing = decreasing = False
    
    for i in range(l, r):
        if arr[i] > arr[i+1]:
            increasing = True
        elif arr[i] < arr[i+1]:
            decreasing = True
            
        if increasing and decreasing:
            return "No"
    
    return "Yes"

# Process each query
for q in queries:
    print(is_ladder(arr, *q))
