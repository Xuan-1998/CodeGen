from collections import defaultdict

def smallest_xor(A, B):
    # Create a memoization table
    dp = defaultdict(int)

    for i in range(A+1):
        for j in range(B+1):
            if i == 0 or j == 0:
                dp[(i,j)] = min(i, j)
            else:
                k = min(i, j)
                while k >= 0 and k <= i and k <= j:
                    dp[(i,j)] = min(dp[(i,j)], dp[(k,i-k+j-k)] + k)
                    k -= 1

    # Find the smallest value of X that satisfies A = X + Y and B = X ^ Y
    for x in range(A+1):
        y = A - x
        if ((x & y) == B):
            return f"{x} {y}"

    # If no solution is found, print -1
    return "-1"

# Read input from stdin
A = int(input())
B = int(input())

# Print the result to stdout
print(smallest_xor(A, B))
