def max_problems(n, k, a):
    left = 0
    right = n - 1
    max_solved = 0
    while left <= right:
        if a[left] <= k and a[right] <= k:
            max_solved += 1
            left += 1
            right -= 1
        elif a[left] > k:
            right -= 1
        else:
            left += 1
    return max_solved

n, k = map(int, input().split())
a = list(map(int, input().split()))
print(max_problems(n, k, a))
