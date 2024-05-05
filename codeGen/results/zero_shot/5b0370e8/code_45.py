import sys

def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        and_count = [0] * (1 << k)

        for _ in range(n):
            x = int(input())
            and_count[x] += 1

        result = 1
        for i in range(1, 1 << k):
            if and_count[i] >= and_count[i - 1]:
                result *= and_count[i]
                break
        print(result % (10**9 + 7))

solve()
