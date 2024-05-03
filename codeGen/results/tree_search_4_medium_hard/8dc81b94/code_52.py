def equalize_array():
    n = int(input())
    array = list(map(int, input().split()))
    
    for i in range(1, n + 1):
        for j in range(n - i + 1):
            if all(x <= 0 for x in array[j:j+i]):
                print("YES")
                return
    print("NO")

equalize_array()
