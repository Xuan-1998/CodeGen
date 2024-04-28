def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + arr[i]
        
        max_partitions = 0
        for i in range(1, n):
            if prefix_sum[i] == prefix_sum[n] - prefix_sum[n - i]:
                max_partitions += 1
        
        print(max_partitions)

if __name__ == "__main__":
    solve()
