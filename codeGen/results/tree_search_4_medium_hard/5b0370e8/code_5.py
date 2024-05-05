def f(i):
    if i < 0:  # base case: 0 when i < 0
        return 1

    memo = {}
    for last_bit in range(2):  # consider pairs of integers with bitwise AND greater than or equal to bitwise XOR and count their combinations
        memo[(i, last_bit)] = f(i - 1) * (2 ** k - 2**last_bit + 1)

    return sum(memo.values())

def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        memo = {}
        result = 0
        for i in range(n):
            last_bit = (int(input()) >> (k - 1)) & 1
            if (i, last_bit) not in memo:
                memo[(i, last_bit)] = f(i)
            result += memo[(i, last_bit)]

        print(result % (10**9 + 7))

if __name__ == "__main__":
    solve()
