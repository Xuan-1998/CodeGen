import sys

def count_arrays():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        nums = list(map(int, sys.stdin.readline().split()))
        
        and_result = 0
        xor_result = 0
        for num in nums:
            and_result |= num
            xor_result ^= num
        
        dp = [[0] * (1 << k) for _ in range(k + 1)]
        for i in range(1, k + 1):
            dp[i][and_result & (1 << i)] += 1
        
        total = 0
        for j in range(k + 1):
            if and_result >= xor_result:
                total += dp[j][xor_result]
        
        print(total % (10**9 + 7))

count_arrays()
