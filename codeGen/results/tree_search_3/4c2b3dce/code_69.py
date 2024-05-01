def solve():
    s = input()
    n = len(s)

    dp = [[False] * (n + 1) for _ in range(n + 1)]

    state = 'NOT_FOUND'
    for i in range(n):
        if state == 'NOT_FOUND':
            if s[i:i+2] == 'AB':
                state = 'FOUND_AB'
            elif s[i:i+2] == 'BA':
                state = 'FOUND_AB'
        else:
            dp[n-1][i] = True

    print('YES' if dp[-1][-1] else 'NO')

solve()
