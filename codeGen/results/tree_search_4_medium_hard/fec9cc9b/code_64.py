def is_ladder():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    state = [[0] * (n + 1) for _ in range(n + 1)]

    max_non_dec = 0
    max_non_inc = 0

    for i in range(1, n + 1):
        for j in range(i):
            if arr[j] <= arr[i]:
                max_non_dec = max(max_non_dec, state[i - 1][j] + 1)
            else:
                max_non_inc = max(max_non_inc, state[i - 1][j])
            state[i][j] = max(max_non_dec, max_non_inc)

    for _ in range(m):
        l, r = map(int, input().split())
        print("Yes" if state[r][r] == state[l - 1][l - 1] else "No")

is_ladder()
