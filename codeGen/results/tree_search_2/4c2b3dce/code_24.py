def checkIfContainsABA(s):
    dp = [[0] * (len(s) + 1) for _ in range(len(s) + 1)]

    for i in range(len(s)):
        if s[i:i+2] == 'AB':
            for j in range(i+3, len(s)+1):
                if s[j-2:j] == 'BA':
                    dp[i][j] = 1
                    break

    return 'YES' if any(dp[i][j] == 1 for i in range(len(s)) for j in range(i+3, len(s)+1)) else 'NO'

# Take input from standard input
s = input()

print(checkIfContainsABA(s))
