def min_changes(s):
    n = len(s)
    k = int(input())
    dp = {}
    
    # Base cases: empty string can be found in any infinite string
    for j in range(k+1):
        dp[(0, j)] = 0
    
    for i in range(1, n+1):
        for j in range(min(i, k)+1):
            if s[i-1] != 'RGB'[j%3]:
                dp[(i, j)] = min(dp.get((i-1, j), float('inf')), dp.get((i-1, j-1), float('inf'))) + 1
            else:
                dp[(i, j)] = dp.get((i-1, j), 0)
    
    return dp[(n, k)]

while True:
    try:
        n, k = map(int, input().split())
        print(min_changes(input()))
    except EOFError:
        break
