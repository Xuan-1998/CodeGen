import math

def isDistinct(seen):
    return len(set(seen)) == len(seen)

def solve():
    T = int(input())
    for _ in range(T):
        n = int(input())
        dp = [[0.0] * (1 << 16) for _ in range(n + 1)]
        for i in range(1, n + 1):
            p, a, b = map(int, input().split())
            if i == 1:
                seen = {a}
                dp[i][seen.bit()] = 1.0 if isDistinct(seen) else 0.0
            else:
                for mask in range(1 << 16):
                    seen = set()
                    for j in range(i):
                        seen.add((dp[j][mask].bit() >> (16 - 4 * j)) % 16)
                    seen.add(a if mask & (1 << 15) else b)
                    dp[i][seen.bit()] += min(dp[j][mask] for j in range(j)) * ((a == b) or p)
        print(sum(1.0 for x in dp[n]) / math.pow(2, n))

if __name__ == "__main__":
    solve()
