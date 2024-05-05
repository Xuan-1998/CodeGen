import math

def count_binary_numbers(n):
    dp = [[False for _ in range(math.ceil(math.log2(i)) + 1)] for i in range(n + 1)]
    
    # Base case: There are no consecutive ones in the binary representation of 0.
    dp[0][0] = True
    
    for i in range(1, n + 1):
        for j in range(math.ceil(math.log2(i))):
            if (i >> j) & 1:
                dp[i][j] = dp[i - (2 ** (j + 1))][j] if j > 0 else True
            else:
                dp[i][j] = True
    
    return sum(1 for i in range(n + 1) if not any(int((i >> j) & 1) == int((i >> (j - 1))) for j in range(math.ceil(math.log2(i)))))

n = int(input())
print(count_binary_numbers(n))
