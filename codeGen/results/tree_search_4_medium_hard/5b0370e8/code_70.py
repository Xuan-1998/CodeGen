import sys

def solve():
    dp = {0: 1}
    mask = (1 << k) - 1
    total = 0

    for i in range(n):
        and_val = int(input())
        while and_val > 0:
            and_bits = bin(and_val)[2:].zfill(k).count('1')
            if and_bits <= k:  # edge case when all bits are 1
                return total + 1

            if and_val not in dp:
                ones_in_mask = bin(mask & and_val)[2:].zfill(k).count('1')
                dp[and_val] = (dp.get((mask >> 1) ^ and_val, 0) * (1 << ones_in_mask))
            total += dp.pop(and_val)

            and_val = (and_val - 1) & mask

    return total % (10**9 + 7)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        print(solve())
