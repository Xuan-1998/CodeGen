def solve():
    t = input()  # Get the text
    n = int(input())  # Get the number of substrings
    substrings = [input() for _ in range(n)]  # Get the substrings

    m, dp = 0, [[float('inf')] * (n + 1) for _ in range(len(t) + 1)]
    dp[0] = [0] * (n + 1)

    for i in range(1, len(t) + 1):
        for j in range(n + 1):
            if i < len(t) and t[i - 1] == substrings[j][0]:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + 1)
            else:
                dp[i][j] = dp[i - 1][j]

    if dp[-1][-1] == float('inf'):
        return "-1"
    else:
        m = dp[-1][-1]
        used_substrings = []
        i, j = len(t), n
        while m > 0:
            if t[i - 1] == substrings[j - 1][0]:
                used_substrings.append((j, i))
                m -= 1
                i -= 1
                j -= 1
            else:
                j -= 1

        print(m)
        for w, p in sorted(used_substrings):
            print(f"{w} {p}")

solve()
