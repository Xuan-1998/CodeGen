python
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
    operations = [[None] * (k + 1) for _ in range(n + 1)]
    
    dp[0][0] = True
    
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if dp[i-1][j-1] and sum(initial_seq[:i]) == sum(final_seq[:j]):
                dp[i][j] = True
                operations[i][j] = (i-1, j-1)
    
    if not dp[n][k]:
        print("NO")
        return
    
    print("YES")
    result_operations = []
    i, j = n, k
    
    while i > 0 and j > 0:
        prev_i, prev_j = operations[i][j]
        if prev_i is not None and prev_j is not None:
            if prev_i != i - 1:
                result_operations.append((prev_i + 1, 'R'))
            elif prev_j != j - 1:
                result_operations.append((prev_i + 1, 'L'))
        i, j = prev_i, prev_j
    
    for op in reversed(result_operations):
        print(f"{op[0]} {op[1]}")


