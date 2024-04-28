def min_recolors(s):
    n = len(s)
    dp = [[False] * (n+1) for _ in range(n+1)]

    for i in range(n+1):
        if i == 0:
            dp[i][0] = True
        else:
            for p in range(i+1):
                if p > 0 and dp[i-1][p-1]:
                    dp[i][p] = True
                elif p == 0:
                    dp[i][p] = False

    min_p = n
    for p in range(n+1):
        if dp[n][p]:
            min_p = p
            break

    recolors = min_p
    t = list(s)
    for i in range(1, n+1):
        if s[i-1] == s[i]:
            t[i] = 'R' if s[i] == 'G' else 'G'
            recolors -= 1

    return str(recolors), ''.join(t)

if __name__ == '__main__':
    n = int(input())
    s = input()
    print(min_recolors(s))
