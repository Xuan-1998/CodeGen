from math import inf
from collections import namedtuple

TestCase = namedtuple('TestCase', 'N')

def solve(test_cases):
    for test_case in test_cases:
        N = test_case.N
        dp = [0] * (N + 1)
        
        # Calculate the expected number of non-zero carries when adding A and B, both with less than or equal to i digits.
        for i in range(1, N + 1):
            for carry in range(10):  # For each possible carry value (0-9), calculate the expected number of non-zero carries based on whether a carry occurs or not.
                dp[i] += min(carry, 9 - carry)
        
        print(dp[N])

if __name__ == "__main__":
    test_cases = []
    T = int(input())
    for _ in range(T):
        N = int(input())
        test_cases.append(TestCase(N))
    
    solve(test_cases)
