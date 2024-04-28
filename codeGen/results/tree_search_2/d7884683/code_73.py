from sys import stdin

def read_input():
    t = int(stdin.readline())
    for _ in range(t):
        n = int(stdin.readline())
        arr = list(map(int, stdin.readline().split()))
        yield n, arr

def solve_case(n, arr):
    total_sum = sum(arr)
    dp = [[0] * (total_sum // 2 + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        left_sum = sum(arr[:i])
        right_sum = total_sum - left_sum
        
        for j in range(min(left_sum, right_sum), -1, -1):
            if dp[i-1][j] == 0:
                dp[i][j + (right_sum - j)] = 1
            elif dp[i-1][j] == 1 and dp[i][j] == 1:
                break
    
    return min(range(dp[-1].index(min(dp[-1])), -1, -1), key=lambda i: dp[-1][i]) // 2

for n, arr in read_input():
    print(solve_case(n, arr))
