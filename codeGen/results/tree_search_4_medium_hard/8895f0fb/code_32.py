from collections import defaultdict

def expected_carries():
    T = int(input())
    memo = defaultdict(int)

    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i == 0 or j == 0:
            return 0
        
        s = (10 - ord('0')) * (i > 0 and A[i-1]) + (10 - ord('0')) * (j > 0 and B[j-1])
        
        carry = min(s, 9) if i > 0 and j > 0 else max(0, s)
        
        memo[(i, j)] = dp(i-1 if i > 0 else 0, j-1 if j > 0 else 0) + (carry >= 10)
        
        return memo[(i, j)]

    for _ in range(T):
        N = int(input())
        A = [int(x) for x in input().split()]
        B = [int(x) for x in input().split()]
        
        expected = sum(dp(i, j) for i in range(N) for j in range(N)) / (N ** 2)
        
        print(f"{expected:.9f}")

if __name__ == "__main__":
    expected_carries()
