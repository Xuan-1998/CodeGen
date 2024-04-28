from collections import defaultdict

def max_points(n, sequence):
    memo = defaultdict(int)
    def dp(i):
        if i < 0:
            return 1
        if i >= n or sequence[i] not in memo:
            memo[sequence[i]] = 1 + min(dp(i-2) if i >= 2 and sequence[i] - 1 in sequence else 0, 
                                          dp(i+2) if i < n - 2 and sequence[i] + 1 in sequence else 0)
        return memo[sequence[i]]

    return max([dp(i) for i in range(n)])

if __name__ == "__main__":
    n = int(input())
    sequence = list(map(int, input().split()))
    print(max_points(n, sequence))
