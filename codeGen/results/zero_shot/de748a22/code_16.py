def min_remove_elements(signs, l, r):
    n = len(signs)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + (1 if signs[i] == "+" else -1)

    total_sum = prefix_sum[r] - prefix_sum[l]
    return abs(total_sum) // 2

while True:
    n, q = map(int, input().split())
    signs = list(input())

    for _ in range(q):
        l, r = map(int, input().split())
        print(min_remove_elements(signs, l, r))
