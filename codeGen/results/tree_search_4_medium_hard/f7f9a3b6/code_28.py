def solve():
    MOD = 10**9 + 7

    n = int(input())
    s = input()
    a = [int(x) for x in input().split()]

    dp = [[0] * (n+1) for _ in range(27)]
    dp[26][0] = 1
    curr_max = 0

    for i in range(n):
        for j in range(i, n):
            if all(s[j].lower() <= chr(x+96) and a[ord(s[j].lower())-97] >= j-i for x in range(26)):
                dp[ord(s[i].lower())-97][j+1] = (dp[ord(s[i].lower())-97][i] + dp[ord(s[i].lower())-97][j]) % MOD
            curr_max = max(curr_max, j-i)

    ans = sum(dp[26])
    print(ans % MOD)
    print(curr_max)
    print(min(i for i in range(n) if not dp[26][i]))

solve()
