import sys

def solve():
    n, k = map(int, input().split())
    and_table = [[0] * (1 << k) for _ in range(n + 1)]
    xor_table = [0] * (1 << k)

    and_table[0][0] = 1
    for i in range(1, n + 1):
        for s in range(1 << k):
            and_table[i][s] = sum(and_table[i - 1][(t & s) | ((~t) & (s >> j)) & ((1 << k) - 1)] for t in range(1 << k))

    xor_table[0] = 1
    for i in range(1, n + 1):
        for j in range(1 << k):
            if j:
                xor_table[j] += sum(xor_table[t] for t in range(j))
            else:
                xor_table[j] = 1

    answer = sum(and_table[n][s] for s in range(1 << k)) - sum(xor_table[j] for j in range(1 << k) if not (j & ((1 << k) - 1)))
    print(answer % (10 ** 9 + 7))

if __name__ == "__main__":
    solve()
