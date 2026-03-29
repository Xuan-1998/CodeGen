from functools import lru_cache

def expected_carries(n):
    @lru_cache(None)
    def dp(n, prev_carry):
        if n == 0:
            return 0
        
        carries = [0] * (n + 1)
        for i in range(1, 11):  # 10 possible digit sums
            carries[i % 10] += 1
        
        result = 0
        for i in range(1, n):
            result += dp(i - 1, (prev_carry + (i > 9)) % 2)
        
        return result
    
    total_carries = 0
    for n in range(n, 0, -1):  # Iterate from N to 1
        total_carries += dp(n - 1, 0) / (10 ** n)
    
    return total_carries

T = int(input())  # Read number of test cases
for _ in range(T):
    N = int(input())  # Read maximum number of digits in A and B
    print(expected_carries(N))
