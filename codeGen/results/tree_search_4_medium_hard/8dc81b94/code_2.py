===BEGIN CODE===
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    left = 0
    right = n - 1
    
    while left <= right:
        if arr[left] + arr[right] > 0:
            arr[0] -= 1
            for i in range(1, n):
                arr[i] += 1
            left += 1
        elif arr[left] + arr[right] < 0:
            arr[n-1] -= 1
            for i in range(n-2, -1, -1):
                arr[i] += 1
            right -= 1
        else:
            if all(i == 0 for i in arr):
                print("YES")
            else:
                print("NO")
            return
    
    print("YES")

solve()
===END CODE===
