import sys

# Define a constant for modulo operation.
MOD = 10**9 + 7

def solve():
    # Read input from stdin.
    t = int(input())

    for _ in range(t):
        n, k = map(int, input().split())
        and_xor = [0] * (1 << k)

        for num in map(int, input().split()):
            for i in range(k - 1, -1, -1):
                bit = (num >> i) & 1
                and_xor[bit] += 1

        count = sum((and_xor[i] + and_xor[-1-i]) % MOD for i in range(len(and_xor) // 2))
        print(count)

if __name__ == "__main__":
    solve()
