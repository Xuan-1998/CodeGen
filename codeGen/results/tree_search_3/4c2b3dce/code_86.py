import sys

def check_strings(s):
    dp = {(True, False): [0, 1], (False, True): [1, 0]}
    for i, c in enumerate(s):
        if c == 'A':
            new_state_A = (dp[dp[i-1][1]][0] == 0)
            new_state_B = dp[i-1][0]
            if new_state_A and not new_state_B:
                return "YES"
            dp[(new_state_A, new_state_B)] = [i+1, i+2]
        elif c == 'B':
            new_state_A = dp[i-1][0]
            new_state_B = (dp[dp[i-1][1]][0] == 1)
            if new_state_A and not new_state_B:
                return "YES"
            dp[(new_state_A, new_state_B)] = [i+1, i+2]
    return "NO"

s = sys.stdin.readline().strip()
print(check_strings(s))
