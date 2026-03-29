import sys

def simulate_program(sequence):
    n = len(sequence)
    dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]

    # Base case: When x <= 0 or x > n, terminate and return y as the final value.
    for i in range(1, n+1):
        if sequence[i-2] <= 0 or sequence[i-2] > n:
            dp[sequence[i-2]][0] = 0
        else:
            dp[sequence[i-2]][0] = 0

    # Fill up the DP table.
    for i in range(1, n+1):
        for j in range(n+1):
            if sequence[i-1] <= 0 or sequence[i-1] > n:
                break
            dp[sequence[i-1]][j] = max(dp[sequence[i-1]+sequence[i-1]][j+sequence[i-1]], 
                                         dp[sequence[i-1]-sequence[i-1]][j+sequence[i-1]])

    return dp[n-1][-1]

def main():
    n = int(input())
    sequence = list(map(int, input().split()))
    print(simulate_program(sequence))

if __name__ == "__main__":
    main()
