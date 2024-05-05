import sys

def min_steps_to_color_text(text, strings):
    n = len(strings)
    dp = [[float('inf')] * (len(text) + 1) for _ in range(len(text) + 1)]
    
    for i in range(len(text), -1, -1):
        for j in range(i + 1):
            dp[i][j] = float('inf')
            
            for k in range(n):
                if text[j:i].find(strings[k]) != -1:
                    dp[i][j] = min(dp[i][j], dp[i - len(strings[k])] [j] + 1)
                    
    if dp[0][0] == float('inf'):
        return -1
    else:
        steps = dp[0][0]
        
        for i in range(len(text), 0, -1):
            for j in range(i):
                if text[j:i].find(strings[k]) != -1 and dp[i][j] == dp[i - len(strings[k])] [j] + 1:
                    k = strings.index(text[j:i])
                    print(f"{k+1} {j}")
        return steps

# Example usage
text = input()
n = int(input())
strings = [input() for _ in range(n)]

steps = min_steps_to_color_text(text, strings)
if steps == -1:
    print(-1)
else:
    print(steps)
    for i in range(steps):
        w, p = map(int, input().split())
        print(f"{w} {p}")
