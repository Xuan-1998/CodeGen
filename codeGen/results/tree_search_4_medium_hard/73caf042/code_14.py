import sys

N = int(sys.stdin.readline())
dp = [[0] * N for _ in range(N)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        room_num = i + j
        even_sum = sum(int(digit) for digit in str(room_num) if int(digit) % 2 == 0)
        odd_sum = sum(int(digit) for digit in str(room_num) if int(digit) % 2 != 0)
        dp[i][j] = abs(even_sum - odd_sum)

print(dp[N-1][N-1])
