import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        dp = [0] * (1 << k)
        and_result = 0
        for _ in range(n):
            num = int(sys.stdin.readline())
            and_result |= num
            while and_result & (1 << k):
                and_result &= ~(1 << k)
            if and_result >= (1 << k) - 1:
                break
        for i in range(1 << k):
            xor_result = and_result ^ i
            count = sum((and_result >> j) & 1 for j in range(k)) - sum((xor_result >> j) & 1 for j in range(k))
            dp[i] = (dp[i - 1] if i > 0 else 0) + count % (10**9 + 7)
        print(dp[-1])

if __name__ == "__main__":
    solve()
