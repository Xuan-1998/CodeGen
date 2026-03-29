import sys

def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        and_count = [0] * (k + 1)
        xor_count = [0] * (k + 1)

        for num in map(int, input().split()):
            for i in range(k, -1, -1):
                if (num >> i) & 1:
                    and_count[i] += 1
                    xor_count[i] ^= 1

        answer = pow(2, k, 10**9 + 7)
        for i in range(k, -1, -1):
            answer *= (and_count[i] * and_count[i] % (10**9 + 7) +
                       xor_count[i]) % (10**9 + 7)

        print(answer)

solve()
