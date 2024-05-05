import sys

def solve():
    t = input().strip()
    n = int(input())
    strings = [input().strip() for _ in range(n)]
    
    dp = {(0, 0): 0}
    min_steps = float('inf')
    
    for i in range(len(t)):
        min_steps_here = float('inf')
        last_used_string = None
        for j in range(n):
            if t[i:].find(strings[j]) != -1:
                last_used_string = j
                new_state = (last_used_string, i + len(strings[last_used_string]))
                dp[new_state] = min(dp.get(new_state, float('inf')), dp[(j, i)] + 1)
                min_steps_here = min(min_steps_here, dp[new_state])
        if min_steps_here == float('inf'):
            print(-1)
            return
        
        min_steps = min(min_steps, min_steps_here)
    
    for _ in range(min_steps):
        last_used_string, last_covered_position = max((k[0], k[1]) for k in dp if dp[k] == min_steps)
        print(f"{last_used_string} {last_covered_position - len(strings[last_used_string])}")
        del dp[(last_used_string, last_covered_position)]
    else:
        print(min_steps)

if __name__ == "__main__":
    solve()
