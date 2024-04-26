MOD = 998244353

def add_mod(a, b):
    return (a + b) % MOD

def main():
    n = int(input().strip())
    A = [input().strip().split() for _ in range(n)]

    # Initialize dp array where dp[i] will represent the sum of all f(B) for subsequences
    # that end before the ith element and where the ith element is the smallest in T.
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: there's one subsequence (empty) before the first element

    for i in range(1, n + 1):
        if A[i - 1][0] == '+':
            x = int(A[i - 1][1])
            # Update dp[i] based on the previous dp values and the contribution of x
            new_dp = [0] * (n + 1)
            for j in range(i + 1):
                new_dp[j] = add_mod(new_dp[j], dp[j])  # When x is not the smallest
                if j > 0:
                    new_dp[j] = add_mod(new_dp[j], dp[j - 1] * x)  # When x is the smallest
            dp = new_dp
        else:
            # If the current element is '-', merge the dp values considering the removal of the smallest element
            for j in range(i):
                dp[j] = add_mod(dp[j], dp[j + 1])

    # Sum up all dp values except dp[0] since it represents the empty subsequence
    result = sum(dp[1:]) % MOD
    print(result)

if __name__ == "__main__":
    main()
