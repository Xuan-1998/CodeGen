n, m = map(int, input().split())
array = list(map(int, input().split()))

for _ in range(m):
    l, r = map(int, input().split())
    is_non_decreasing = True
    is_non_increasing = True
    
    for i in range(l-1, r):
        if array[i] > array[i+1]:
            is_non_decreasing = False
        if array[i] < array[i+1]:
            is_non_increasing = False
    
    if is_non_decreasing and is_non_increasing:
        print("Yes")
    else:
        print("No")
