def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    a = list(map(int, data[1:n+1]))
    k = int(data[n+1])
    b = list(map(int, data[n+2:n+2+k]))
    
    if sum(a) != sum(b):
        print("NO")
        return

    dp = [[False] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = True
    
    for i in range(n):
        for j in range(k):
            if not dp[i][j]:
                continue
            current_sum = 0
            for l in range(i, n):
                current_sum += a[l]
                if current_sum == b[j]:
                    dp[l + 1][j + 1] = True
    
    if not dp[n][k]:
        print("NO")
        return

    print("YES")
    operations = []
    i, j = n, k
    while j > 0:
        current_sum = 0
        for l in range(i-1, -1, -1):
            current_sum += a[l]
            if current_sum == b[j-1]:
                for m in range(l, i-1):
                    if a[m] < a[m+1]:
                        operations.append((m+1, 'R'))
                        a[m+1] += a[m]
                    else:
                        operations.append((m+2, 'L'))
                        a[m] += a[m+1]
                i = l
                j -= 1
                break
    
    for op in operations:
        print(op[0], op[1])


