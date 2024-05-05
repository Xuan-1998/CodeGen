def solution():
    n, q = map(int, input().split())
    signs = list(input())
    queries = [list(map(int, input().split())) for _ in range(q)]

    sign_sum = [0] * (n + 1)
    for i in range(n):
        if signs[i] == '+':
            sign_sum[i + 1] = sign_sum[i] + 1
        else:
            sign_sum[i + 1] = sign_sum[i] - 1

    for l, r in queries:
        total_signs = sign_sum[r] - sign_sum[l]
        min_to_remove = abs(total_signs)
        print(min_to_remove)

solution()
