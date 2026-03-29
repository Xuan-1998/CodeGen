# Step 1: Read input
n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = []
for _ in range(m):
    queries.append(tuple(map(int, input().split())))

# Step 2: Define a function to check if the subsegment is a ladder
def is_ladder(arr, l, r):
    # Check if the first half of the subsegment doesn't decrease
    for i in range(l, (r+1)//2):
        if arr[i] < arr[i-1]:
            return False
    
    # Check if the second half of the subsegment doesn't increase
    for i in range((r+1)//2, r+1):
        if arr[i] > arr[i-1]:
            return False
    
    return True

# Step 3: Process each query and print the answer
for l, r in queries:
    if is_ladder(arr, l, r):
        print("Yes")
    else:
        print("No")
