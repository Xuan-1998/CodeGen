import math

def count_valid_binary(n):
    total_count = 0
    for k in range(math.floor(math.log2(n)) + 1):
        dp = [True] + [False] * (1 << k)
        for i in range(1, 1 << k):
            if i & (i >> 1):  # Check for consecutive ones
                continue
            valid = True
            for j in range(k):
                if i & (1 << j) and not dp[j]:
                    valid = False
                    break
            dp[i] = valid
        total_count += sum(dp)
    return total_count

n = int(input())
print(count_valid_binary(n))
