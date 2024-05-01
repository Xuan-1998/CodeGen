def solve():
    s = input()
    dp = [[False, False] for _ in range(2)]

    for i in range(len(s)):
        if i < 2:
            if s[i] == 'A':
                dp[0][0] = True
            else:
                dp[1][1] = True
        else:
            if s[i] == 'A' and not dp[1][1]:
                dp[0][0] = True
            elif s[i] == 'B' and not dp[0][0]:
                dp[1][1] = True

    print("YES" if all([dp[0][0], dp[1][1]]) else "NO")

if __name__ == "__main__":
    solve()
