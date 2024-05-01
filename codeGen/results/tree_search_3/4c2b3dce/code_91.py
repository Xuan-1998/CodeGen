===BEGIN CODE===
from collections import defaultdict

def solve():
    s = input()
    dp = defaultdict(bool)

    for i in range(len(s)):
        if i >= 2 and (s[i-1:i+1] == 'AB' or s[i-1:i+1] == 'BA'):
            if not dp[(True, True)]:
                dp[(True, True)] = True
        elif s[i] == 'A':
            if not dp[False]:
                dp[False] = True
            dp[(True, False)] = not dp.get((True, False), False)
        else:
            if not dp[False]:
                dp[False] = True
            dp[(False, True)] = not dp.get((False, True), False)

    if (True, True) in dp or (True, False) in dp:
        print('YES')
    else:
        print('NO')

solve()
===END CODE===
