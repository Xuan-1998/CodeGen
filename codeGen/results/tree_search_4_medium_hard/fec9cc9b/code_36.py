def check_ladder(array, l, r):
    min_val = min(array[l-1:r])
    max_val = max(array[l-1:r])
    
    if array[l-1] <= array[r-1] and array[0] <= min_val:
        return True
    elif array[l-1] >= array[r-1] and array[n-1] >= max_val:
        return True
    else:
        return False

n, m = map(int, input().split())
array = list(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(m)]

for query in queries:
    l, r = query
    if check_ladder(array, l, r):
        print("Yes")
    else:
        print("No")
