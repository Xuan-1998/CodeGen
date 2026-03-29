def digit_sum(n):
    return sum(int(digit) for digit in str(n))

def total_diamonds(N):
    dp = [[0] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                continue
            elif i == 0 or j == 0:
                dp[i][j] = dp[max(0, i-1)][max(0, j-1)]
            else:
                dp[i][j] = abs(digit_sum(i + j) - digit_sum((i//2)*2 + (j//2)*2))
    
    total = 0
    for row in dp:
        total += sum(row)
    
    return total

T = int(input())
for _ in range(T):
    N = int(input())
    print(total_diamonds(N))
