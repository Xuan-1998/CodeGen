def color_text_red(input):
    t = input().strip()
    n = int(input())
    strings = [input().strip() for _ in range(n)]

    dp = [[[float('inf')] * (len(t) + 1) for _ in range(len(strings) + 1)] for _ in range(len(t) + 1)]
    last_used = [[-1] * (len(t) + 1) for _ in range(len(t) + 1)]

    dp[0][0][0] = 0
    memo = {}

    def update_dp(i, j, k):
        if i > len(t) or j > n:
            return float('inf')
        key = (j - 1, k - 1)
        if key in memo:
            return memo[key]
        if k < 0:
            return 1
        min_steps = float('inf')
        for string_index in range(j):
            if strings[string_index][0] == t[k:]:
                if dp[i-1][string_index][k+len(strings[string_index])] < float('inf'):
                    min_steps = min(min_steps, update_dp(i-1, string_index, k+len(strings[string_index]))))
        memo[key] = min_steps + 1
        return memo[key]

    for i in range(len(t) + 1):
        for j in range(n + 1):
            for k in range(len(t) + 1):
                dp[i][j][k] = update_dp(i, j, k)

    if dp[-1][-1][-1] >= len(t):
        return -1

    m = dp[-1][-1][-1]
    used_strings = []
    last_covered_position = len(t)
    for i in range(m-1, -1, -1):
        for j in range(n):
            if dp[i][j][last_covered_position] < float('inf'):
                used_strings.append((j, last_covered_position))
                last_covered_position -= len(strings[j])
                break
        else:
            continue
        break

    print(m)
    for i, (string_index, position) in enumerate(reversed(used_strings)):
        print(string_index, position)

color_text_red()
