mod = int(1e9) + 7

def solve(a, b):
    dp = {(0, 0, 0): 0}
    
    for i in range(len(bin(a)) - 2):
        carry = 0
        for j in range(i + 1):
            x = (a >> j) & 1
            y = (b >> (i - j)) & 1
            state = (x, y, carry)
            if state not in dp:
                if x and y:
                    dp[state] = (dp.get((0, 0, 0), 0) + mod) % mod
                elif x or y:
                    dp[state] = (dp.get((0, 0, 1), 0) + mod) % mod
                else:
                    dp[state] = (dp.get((0, 0, 0), 0)) % mod
            carry = ((x and not y) or (y and not x)) and 1
        if (carry and i < len(bin(b)) - 2):
            for j in range(i + 1):
                x = (a >> j) & 1
                y = (b >> (i - j)) & 1
                state = (x, y, carry)
                if state not in dp:
                    if x and y:
                        dp[state] = (dp.get((0, 0, 0), 0) + mod) % mod
                    elif x or y:
                        dp[state] = (dp.get((0, 0, 1), 0) + mod) % mod
                    else:
                        dp[state] = (dp.get((0, 0, 0), 0)) % mod
                carry = ((x and not y) or (y and not x)) and 1
    
    return sum(dp.values()) % mod

a = int(input())
b = int(input())

print(solve(a, b))
