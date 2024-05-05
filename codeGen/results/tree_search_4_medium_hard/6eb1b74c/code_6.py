dp = [[float('inf')] * (len(t) + 1) for _ in range(n + 1)]
used_strings = set()

def dfs(i, j):
    if dp[i][j] != float('inf'):
        return dp[i][j]
    
    count = 0
    used_strings_copy = used_strings.copy()
    
    for s in strings:
        if t[i:j+1].startswith(s):
            count += 1 + dfs(i-s, j-len(s))
            used_strings_copy.add(s)
            break
    
    else:
        return float('inf')
    
    dp[i][j] = count
    return count

min_steps = float('inf')

for i in range(n+1):
    for j in range(len(t), -1, -1):
        if dfs(i, j) < min_steps:
            min_steps = dfs(i, j)

if min_steps == float('inf'):
    print(-1)
else:
    used_strings.clear()
    count = 0
    i, j = n, len(t)-1
    
    while i > 0 and j >= 0:
        for s in strings:
            if t[i-1:j+1].startswith(s):
                used_strings.add(s)
                count += 1
                i -= len(s)
                break
        else:
            i -= 1
            j -= 1
    
    print(min_steps)
    while count > 0:
        for s in strings:
            if t[i-1:i+len(s)-1].startswith(s):
                print(f"{str(used_strings.index(s)+1)} {i}")
                used_strings.remove(s)
                i -= len(s)
                break
        count -= 1
