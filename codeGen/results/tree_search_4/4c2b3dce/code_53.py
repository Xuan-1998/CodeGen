def checkAB(s):
    n = len(s)
    dp = {0: True}

    for i in range(1, n+1):
        if s[i-1:i+1] == 'BA':
            dp[i] = dp.get(i-2, False) and True
        elif s[i-2:i] == 'AB':
            dp[i] = dp.get(i-3, False) or True
        else:
            dp[i] = dp.get(i-1, False)

    return "YES" if dp[n] else "NO"

# Read the input from standard input
s = input().strip()

print(checkAB(s))
