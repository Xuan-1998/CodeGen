import sys

# Initialize memoization dictionary
memo = {}

def dfs(n, prev_val):
    if (n, prev_val) in memo:
        return memo[(n, prev_val)]

    # If the previous value is 0, we can append any number to the end of the sequence
    if prev_val == 0:
        result = "YES"
    else:
        # Check if there exists a segment in $a$ whose length equals prev_val
        for i in range(1, n):
            if i == prev_val:
                result = "YES"
                break
        else:
            result = "NO"

    memo[(n, prev_val)] = result
    return result

# Read input and solve each test case
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    b = list(map(int, sys.stdin.readline().split()))
    prev_val = 0
    for i in range(n):
        if dfs(i + 1, b[i]):
            print("YES")
            break
    else:
        print("NO")
