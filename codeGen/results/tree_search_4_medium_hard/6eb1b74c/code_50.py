from collections import defaultdict

def solve(t, s):
    dp = defaultdict(int)
    dp[("", 0)] = 0
    
    for start_index in range(len(t)):
        for end_index in range(start_index, len(t)):
            substring = t[start_index:end_index+1]
            if any(substring.startswith(s) and len(substring) == len(s) for s in s):
                dp[(t, start_index)] = min(dp.get((substring, 0), float('inf')), end_index - start_index + 1)
    
    memo = {}
    def dfs(text, start_index):
        if (text, start_index) in memo:
            return memo[(text, start_index)]
        
        if start_index >= len(text):
            return 0
        
        dp_val = dp.get((text[:start_index], start_index), float('inf'))
        min_steps = float('inf')
        best_strings = []
        
        for i, s in enumerate(s):
            end_index = text.find(s, start_index)
            if end_index != -1:
                steps = dfs(text[end_index+len(s):], end_index+len(s))
                if steps != -1 and (dp_val + 1 <= min_steps or not best_strings):
                    min_steps = dp_val + 1
                    best_strings = [(i, start_index)]
                elif steps == -1:
                    return -1
        
        memo[(text, start_index)] = min_steps if min_steps != float('inf') else -1
        return memo[(text, start_index)]
    
    result = dfs(t, 0)
    if result == -1:
        print(-1)
    else:
        steps = result
        i = 0
        while steps > 0:
            for j in range(len(s)):
                end_index = t.find(s[j], i)
                if end_index != -1:
                    i = end_index+len(s[j])
                    steps -= 1
                    print(f"({j}, {i})")
                    break
