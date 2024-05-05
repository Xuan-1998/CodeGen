def max_earnings(n, k, c, p):
    dp = [[[0] * (k+1) for _ in range(k+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, k+1):
            for z in range(j, min(i, k)+1):
                if p[i-1][0] <= z and p[i-1][1] <= (z*(z+1)//2)*c:
                    dp[i][j][z] = max(dp[i-1][j-1][z-1] + p[i-1][1], 0)
                else:
                    dp[i][j][z] = dp[i-1][j][z]

    res = [i[1] for i in enumerate(sorted(((i,j) for i in range(n+1) for j in range(k+1) if dp[i][j][-1]), key=lambda x: x[1], reverse=True))][0]
    m = 0
    while res > 0:
        z = k-1
        for i in range(res, -1, -1):
            if dp[i][z][-1] == res and p[i-1][0] <= z:
                print(f"Request {i} to table {z}")
                m += 1
                res -= p[i-1][0]
                z -= 1
        for i in range(n, -1, -1):
            if dp[i][k-1][-1] == res and p[i-1][0] <= k-1:
                print(f"Request {i} to table {k-1}")
                m += 1
                res -= p[i-1][0]
        return [m, res]

# Example usage
n = int(input())
p = []
for _ in range(n):
    group_size, money_spent = map(int, input().split())
    p.append([group_size, money_spent])
k = int(input())
c = int(input())

print(*max_earnings(n, k, c, p))
