def find_equal_elements():
    n = int(input())
    arr = list(map(int, input().split()))
    
    equal_indices = {i for i in range(1, n+1) if i == arr[i-1]}
    
    print(list(equal_indices))

find_equal_elements()
