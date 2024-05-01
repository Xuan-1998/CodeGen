def solve():
    n = int(input())
    s = input()

    dp = [[False] * (1 << n) for _ in range(n + 1)]

    for i in range(n + 1):
        if i == 0:
            continue
        for j in range(1 << n):
            if not dp[i - 1][j]:
                continue
            if s[i - 1] == '0':
                dp[i][j | (1 << (s.count('0') - 1))] = True
            else:
                for k in range(n):
                    if not ((j >> k) & 1):
                        dp[i][j | (1 << k)] = True

    winning_teams = []
    for j in range(1 << n):
        if dp[n][j]:
            winning_teams.append(bin(j)[2:].zfill(n).count('1'))

    print('\n'.join(map(str, sorted(winning_teams))))


if __name__ == "__main__":
    solve()
