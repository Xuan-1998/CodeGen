import sys

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        prefix_sum = [0]
        for num in arr:
            prefix_sum.append(prefix_sum[-1] + num)
        
        dp = [0]
        max_partition = 0
        for i in range(1, n+1):
            if prefix_sum[i] == prefix_sum[n-i]:
                dp.append(dp[-1] + 1)
            else:
                dp.append(max(dp[-1], 1))
            max_partition = max(max_partition, dp[-1])
        
        print(max_partition)

if __name__ == "__main__":
    solve()
