def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    left, right = 0, n-1
    count = 0
    
    while left <= right:
        if a[left] <= k and (right == n-1 or a[right] > k):
            count += 1
            if a[left] <= k:
                left += 1
            else:
                right -= 1
        elif a[right] <= k and (left == 0 or a[left] > k):
            count += 1
            if a[right] <= k:
                right -= 1
            else:
                left += 1
        else:
            break
    
    print(count)

if __name__ == "__main__":
    solve()
