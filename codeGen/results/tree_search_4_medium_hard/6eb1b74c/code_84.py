from collections import defaultdict

def dp(text, strings, covered):
    memo = defaultdict(int)
    def dfs(left, right):
        if not left:
            return len(right)
        if (left, right) in memo:
            return memo[(left, right)]
        
        steps = float('inf')
        for s in right:
            if left.startswith(s):
                steps = min(steps, 1 + dfs(left[len(s):], set(right) - {s}))
        
        memo[(left, right)] = steps
        return steps
    
    return dfs(text, set(strings))

text = input()
n = int(input())
strings = [input() for _ in range(n)]
print(dp(text, strings, 0))
