import sys

def calculate_answer(N, M):
    dp = [0] * (M + 1)

    for i in range(1, M+1):
        dp[i] = sum(dp[j] for j in range(i)) % (10**9 + 7)

    answer = sum(dp)
    print(answer % (10**9 + 7))

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    calculate_answer(N, M)
