from functools import lru_cache

@lru_cache(maxsize=None)
def count_carries(sum):
    if sum <= 9:  # base case: no non-zero carries
        return 0
    
    total_carry = 0
    for a in range(1, 10):  # iterate through A's current digit
        for b in range(10):  # iterate through B's current digit
            if a + b >= 10:
                total_carry += count_carries(sum - a - b)  # recursive step: add carry from previous addition
    
    return total_carry

def solve(N):
    dp = [0] * (10 * N + 1)
    
    for i in range(10 * N, -1, -1):  # iterate through all possible sums
        dp[i] = count_carries(i)  # calculate total number of non-zero carries for this sum
    
    return sum(dp) / (10 ** (2 * N))  # calculate average number of non-zero carries

T = int(input())  # read the number of test cases
for _ in range(T):
    N = int(input())  # read the maximum number of digits in A and B
    print(solve(N))  # print the expected number of non-zero carries
