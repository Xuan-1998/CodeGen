# Step 3: Print answers for each query
for query in queries:
    start, end = query
    print(is_ladder(arr, start-1, end))
