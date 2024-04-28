def max_points(a):
    n = len(a)
    dp_sum = [0] * (n + 1)
    dp_used = [False] * (n + 1)

    for i in range(1, n + 1):
        dp_sum[i] = dp_sum[i-1] + a[i-1]
        if i >= 3:
            dp_used[i] = all(a[j+1] - a[j-1] == a[i] - a[0] for j in range(i-2))

    max_points = [0] * (n + 1)
    max_points[n] = 0

    for i in range(n - 1, -1, -1):
        if dp_used[i]:
            max_points[i] = max_points[i+1]
        else:
            max_points[i] = max(max_points[i+1], max_points[i+2] + a[i])

    return max_points[0]

# Example usage
n = int(input())
a = [int(x) for x in input().split()]
print(max_points(a))
