def solve():
    t = int(input())  # Read the number of test cases
    memo = {}  # Initialize the memoization dictionary

    def dp(n, m):
        if (n, m) in memo:
            return memo[(n, m)]  # Return the cached result

        if n == 0:  # Base case: an empty string has length 0
            return 0

        res = float('inf')  # Initialize the result as infinity
        for i in range(n):
            new_n = (i + 1) % 10  # Apply the operation to each digit
            if m > 0:
                res = min(res, dp(new_n, m - 1))  # Recursively apply the operation
            else:
                return n  # If no more operations are needed, return the current length

        memo[(n, m)] = res  # Cache the result
        return res

    for _ in range(t):
        n, m = map(int, input().split())  # Read the number and operations
        print(dp(n, m) % (10**9 + 7))  # Apply the operation and print the result

if __name__ == "__main__":
    solve()
