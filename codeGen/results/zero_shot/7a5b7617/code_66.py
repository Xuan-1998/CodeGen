import math

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    total_sum = (N - 1) * M
    count = 0
    for s in range(M+1):
        if s <= total_sum:
            count += math.factorial(total_sum) // ((total_sum-s) * math.factorial(s))
    print(count % 1000000000)
