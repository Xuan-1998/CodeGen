import sys

# Define the modulus value
MOD = 10**9 + 7

def solve():
    # Read input
    N, M, C = map(int, input().split())
    upper_radii = list(map(int, input().split()))
    lower_radii = list(map(int, input().split()))

    # Initialize dp_upper and dp_lower arrays
    dp_upper = [0] * (C + 1)
    dp_lower = [0] * (C + 1)

    # Fill up the dp_upper array
    for r in range(1, C + 1):
        if not upper_radii:
            dp_upper[r] = dp_upper[r - 1]
        else:
            k = upper_radii.count(r)
            dp_upper[r] = (dp_upper[r - 1] * (C - r + 1)) % MOD + k

    # Fill up the dp_lower array
    for r in range(1, C + 1):
        if not lower_radii:
            dp_lower[r] = dp_lower[r - 1]
        else:
            k = lower_radii.count(r)
            dp_lower[r] = (dp_lower[r - 1] * (C - r + 1)) % MOD + k

    # Calculate the answer for each test case
    ans = sum([(a + b) % MOD for a, b in zip(dp_upper, dp_lower)])

    # Print the answer
    print(ans)

if __name__ == "__main__":
    solve()
