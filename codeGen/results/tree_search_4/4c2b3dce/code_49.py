from collections import defaultdict

def solve():
    s = input()
    dp = defaultdict(bool)

    for i in range(len(s)):
        state = (s[i] == 'A', s[i] == 'B')
        if state[0]:
            if state[1]:
                dp[(False, False)] = True
            elif i > 0 and dp.get((True, False), False):
                dp[state] = True
        else:
            if state[1]:
                if i > 0 and dp.get((False, True), False) and s[i-1] == 'A':
                    dp[state] = True
                elif i < len(s)-1 and dp.get((True, False), False):
                    dp[state] = True
            else:
                if i < len(s)-1 and dp.get((False, True), False):
                    dp[(state[0], state[1])] = True

    return "YES" if any(dp.values()) else "NO"

print(solve())
