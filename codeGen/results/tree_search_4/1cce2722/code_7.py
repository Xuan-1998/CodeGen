memo = {}

def max_points_affecting_index(n):
    if n <= 1:
        return 0
    if n in memo:
        return memo[n]

    result = 0
    for i in range(1, n):
        if a[i] != a[0]:
            break

    left_max = max_points_affecting_index(i-1)
    right_max = max_points_affecting_index(n-i)

    result = max(left_max, right_max) + i
    memo[n] = result
    return result

n = int(input())
a = list(map(int, input().split()))
print(max_points_affecting_index(n))
