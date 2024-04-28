import sys

def solve(n):
    s = input()
    dp = {0: [2**i - 1 for i in range(n)]}
    
    for i in range(1, n+1):
        next_dp = {}
        for j in range(len(dp)):
            state = list(dp[j])
            if s[i-1] == '1':
                state[0] += 2**(n-i)
            else:
                state[-1] -= 2**(n-i)
            
            key = tuple(state)
            next_dp[key] = dp[j][:state.count(1)]
        dp = next_dp
    
    return '\n'.join(map(str, sorted(set(tuple(sorted(x)) for x in dp.values()))))

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    print(solve(n))
