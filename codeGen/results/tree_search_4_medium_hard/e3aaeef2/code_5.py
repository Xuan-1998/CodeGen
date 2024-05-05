def find_length(n, m):
    memo = {}

    def helper(state):
        if state in memo:
            return memo[state]
        
        n, m = state

        if m == 0:
            return len(str(n))

        next_state = (int(str(n)[0]) + 1) * 10 ** (len(str(n)) - 1) + sum(int(digit) + 1 for digit in str(n)[1:]), m - 1
        
        memo[state] = helper(next_state)
        
        return memo[state]

    return helper((n, m))

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    
    print(find_length(n, m) % (10**9 + 7))
