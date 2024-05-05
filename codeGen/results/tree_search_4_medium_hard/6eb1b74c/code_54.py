from collections import defaultdict

def color_text_red(t, s):
    n = len(s)
    dp = [[-1] * (n + 1) for _ in range(len(t) + 1)]
    memo = {}
    
    def dfs(text_index, remaining_substrings):
        if (text_index, tuple(remaining_substrings)) in memo:
            return memo[(text_index, tuple(remaining_substrings))]
        
        if text_index >= len(t) or not remaining_substrings:
            return -1
        
        min_steps = float('inf')
        for i, s_i in enumerate(s):
            if t[text_index:].startswith(s_i):
                steps = 1 + dfs(text_index + len(s_i), remaining_substrings[:i] + remaining_substrings[i+1:])
                min_steps = min(min_steps, steps)
        
        memo[(text_index, tuple(remaining_substrings))] = min_steps
        return min_steps
    
    min_steps = dfs(0, s)
    
    if min_steps == -1:
        print(-1)
    else:
        for text_index in range(len(t)):
            for i, s_i in enumerate(s):
                if t[text_index:].startswith(s_i):
                    dp[text_index][i] = 1 + dp[text_index + len(s_i)][i-1]
        
        sequence = []
        steps = min_steps
        while steps > 0:
            for text_index in range(len(t)):
                for i, s_i in enumerate(s):
                    if dp[text_index][i] == steps:
                        sequence.append((i, text_index))
                        break
                else:
                    continue
                break
            steps -= 1
        
        print(min_steps)
        for w, p in sequence:
            print(w, p)
