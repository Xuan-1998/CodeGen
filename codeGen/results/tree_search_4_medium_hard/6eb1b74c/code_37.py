def solve():
    t = input().strip()
    n = int(input())
    strings = [input().strip() for _ in range(n)]

    dp = [[float('inf')] * (len(t) + 1) for _ in range(len(t) + 1)]
    dp[0][0] = 0

    for i in range(1, len(t) + 1):
        for j in range(i):
            if t[j:i] in strings:
                dp[i][j] = min(dp[i][j], dp[j+len(s)-1][i+len(s)-1] + 1)

    m = float('inf')
    prev_end = -1
    used_strings = set()

    for i in range(len(t) + 1):
        if all(s not in t[:i] for s in strings):
            return -1

        for j in range(i-1, -1, -1):
            if dp[i][j] != float('inf'):
                m = min(m, dp[i][j])
                used_strings.add(strings.index(t[j:i]))
                prev_end = i
                break

    print(m)

    for j in range(1, m+1):
        w_j = list(used_strings).index(j-1)
        p_j = prev_end - len(strings[w_j]) + 1
        print(f"{w_j} {p_j}")

solve()
