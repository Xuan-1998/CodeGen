# Read the input
n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = []
for _ in range(m):
    l, r = map(int, input().split())
    queries.append((l-1, r))

# Initialize a variable to store whether we are currently in an increasing or decreasing sequence
is_increasing = None

# Iterate over the array for each query
for i, (l, r) in enumerate(queries):
    # Check if we are still in the same sequence as the previous query
    if is_increasing is not None:
        # If we're currently in an increasing sequence and encounter a decrease, or vice versa, it's not a ladder
        if (is_increasing and arr[i] <= arr[l]) or (not is_increasing and arr[i] >= arr[l]):
            print("No")
        # If the current element is equal to the last element of the previous query, we can continue the sequence
        elif i > 0 and arr[i-1] == arr[l]:
            if arr[i] <= arr[l]: 
                is_increasing = True
            else:
                is_increasing = False
        # If it's not equal to the last element of the previous query, we start a new sequence
        else:
            if arr[i] >= arr[l]: 
                is_increasing = True
            else:
                is_increasing = False
    # If this is the first query or we're restarting the sequence, just check the query
    else:
        if arr[l] <= arr[r]:
            print("Yes" if all(arr[i] <= arr[i+1] for i in range(l, r)) else "No")
        else:
            print("Yes" if all(arr[i] >= arr[i-1] for i in range(r, l, -1)) else "No")

    is_increasing = None
