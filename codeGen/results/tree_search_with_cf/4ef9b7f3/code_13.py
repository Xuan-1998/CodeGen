def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    initial_seq = list(map(int, data[1:n+1]))
    k = int(data[n+1])
    final_seq = list(map(int, data[n+2:n+2+k]))
    
    if sum(initial_seq) != sum(final_seq):
        print("NO")
        return
    
    dp = [[False] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = True
    
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if dp[i - 1][j]:
                dp[i][j] = True
            if dp[i][j - 1] and (j == 1 or final_seq[j - 1] == final_seq[j - 2] + initial_seq[i - 1]):
                dp[i][j] = True
    
    if not dp[n][k]:
        print("NO")
        return
    
    print("YES")
    operations = []
    i, j = n, k
    
    while i > 0 and j > 0:
        if dp[i - 1][j]:
            i -= 1
        else:
            if j > 1 and final_seq[j - 1] == final_seq[j - 2] + initial_seq[i - 1]:
                operations.append((i, 'L'))
                initial_seq[i - 2] += initial_seq[i - 1]
                initial_seq.pop(i - 1)
                j -= 1
            else:
                operations.append((i, 'R'))
                initial_seq[i] += initial_seq[i - 1]
                initial_seq.pop(i - 1)
                i -= 1
                j -= 1
    
    for op in reversed(operations):
        print(op[0], op[1])


