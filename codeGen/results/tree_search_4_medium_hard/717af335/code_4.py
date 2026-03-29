def solve():
    A = int(input())
    B = int(input())
    
    dp = [[False] * (B + 1) for _ in range(A + 1)]
    
    # Base cases
    for i in range(A + 1):
        if i <= B:
            dp[i][i ^ B] = True
    
    # Fill the dp array
    for i in range(1, A + 1):
        for j in range(B + 1):
            for x in range(i + 1):
                y = i - x
                if x >= y and (j == x ^ y or dp[x][j]):
                    dp[i][j] = True
    
    # Find the minimum X
    min_x = A
    for i in range(A, -1, -1):
        for j in range(B + 1):
            if dp[i][j]:
                min_x = min(min_x, i)
                break
        else:
            continue
        break
    
    return "-1" if min_x == A else "{} {}".format(min_x, A - min_x)

print(solve())
