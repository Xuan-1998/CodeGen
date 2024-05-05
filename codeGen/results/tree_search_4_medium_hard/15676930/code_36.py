def max_joy(a, b, c):
    n = len(a)
    dp = {}

    def rec(i, k):
        if (i, k) in dp:
            return dp[(i, k)]
        if i == 0:
            # Base case: no hares or only one hare
            return a[i] if k == 0 else c[i]
        total_joy = max(rec(i-1, k), rec(i-1, k-1) + b[i]) if k > 0 else a[i]
        dp[(i, k)] = total_joy
        return total_joy

    # Initialize the DP dictionary with base cases
    for i in range(n):
        dp[(i, 0)] = a[i] if i == 0 or i == n-1 else c[i]
        dp[(i, 1)] = b[i] if i == 0 or i == n-1 else a[i]

    # Compute the maximum total joy for each state
    max_total_joy = 0
    for k in range(3):
        max_total_joy += rec(n-1, k)

    return max_total_joy

# Read input from stdin and print the answer to stdout
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

print(max_joy(a, b, c))
