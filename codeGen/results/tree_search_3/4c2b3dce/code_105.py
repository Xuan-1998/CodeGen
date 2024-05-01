def has_ab_and_ba(s):
    n = len(s)
    
    def dp(i, prev_state):
        if i == n:
            return False
        
        next_state = (prev_state[0] != s[i], s[i])
        
        if (next_state in memo):
            return memo[next_state]
        
        memo[next_state] = False
        for j in range(1 + i // 2, min(n - i, 2) + 1):
            if s[i:i+j].endswith("AB") and s[i+j:i+2*j-1].startswith("BA"):
                memo[next_state] = True
                return True
        
        memo[next_state] = False
        return False
    
    memo = {}
    for i in range(n // 2 + 1):
        if dp(i, ("_", "_")):
            return "YES"
    
    return "NO"

# Read the input from stdin and print the output to stdout.
s = input()
print(has_ab_and_ba(s))
