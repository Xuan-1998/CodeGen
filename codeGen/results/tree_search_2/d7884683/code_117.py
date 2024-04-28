import sys

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + arr[i]
        
        max_partitions = 0
        left_sum = 0
        for i in range(n):
            right_sum = prefix_sum[n] - left_sum
            if left_sum == right_sum:
                max_partitions += 1
            left_sum += arr[i]
        
        print(max_partitions)

solve()
