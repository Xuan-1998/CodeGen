from collections import defaultdict

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + arr[i]
        
        dp = defaultdict(int)
        for i in range(1, n + 1):
            for j in range(i):
                if prefix_sum[i] - prefix_sum[j] == 0:
                    dp[(j, i)] = max(dp.get((j, i), 0) + 1, 1)
        
        print(max(dp.values(), default=0))

if __name__ == "__main__":
    solve()
