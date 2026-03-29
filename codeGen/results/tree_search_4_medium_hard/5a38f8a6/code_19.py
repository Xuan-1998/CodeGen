import math

def min_squares(n):
    memo = {0: 0}
    for i in range(1, n+1):
        if math.sqrt(i) % 1 == 0:
            memo[i] = 1
        else:
            min_squares = float('inf')
            for j in range(1, int(math.sqrt(i))+1):
                if j*j <= i and i - j*j >= 0:
                    min_squares = min(min_squares, 1 + memo.get(i-j*j, float('inf')))
            memo[i] = min_squares
    return memo[n]

n = int(input())
print(min_squares(n))
