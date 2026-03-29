from collections import defaultdict

def get_expected_carries():
    n = int(input())
    
    memo = defaultdict(int)
    memo[0, 0] = 0
    
    for _ in range(n):
        a, b = map(int, input().split())
        
        @lru_cache(None)
        def dp(n, m):
            if (n, m) not in memo:
                carry_sum = 0
                for i in range(min(n, m), -1, -1):
                    last_digit_a = a % 10
                    last_digit_b = b % 10
                    total_carry = min(9 - max(last_digit_a, last_digit_b), (last_digit_a + last_digit_b) // 10)
                    carry_sum += total_carry
                    a //= 10
                    b //= 10
                memo[(n, m)] = carry_sum
            return memo[(n, m)]
        
        expected_carries = dp(a, b)
        print(f"{expected_carries:.6f}")
