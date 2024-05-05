def calculate_beauty Contest(t, l, r):
    # Calculate f(n) for all n from l to r
    beauty_scores = {}
    for i in range(l, r + 1):
        beauty_scores[i] = beauty_scores.get(i, 0) + 1
    
    result = 0
    for i in range(t):
        if i == 0:
            result += beauty_scores[l]
        else:
            result += (i * beauty_scores[l + i - 1])
    
    return result % (10**9 + 7)

t, l, r = map(int, input().split())
print(calculate_beauty Contest(t, l, r))
