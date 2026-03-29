import sys

# Base case: when n = 1, F only takes a single value depending on the last integer in the sequence
def f_base_case(n, s):
    if n == 1:
        return s * (s - a[n])

# Recursive function to calculate F for the current state
def f_recursive(n, s, a_n):
    if n == 1:
        return f_base_case(1, s)
    else:
        min_f = float('inf')
        for x_i in range(s + 1):
            y_i = a_n - x_i
            # Calculate F for the current state and update min_f
            min_f = min(min_f, f_recursive(n-1, s-x_i, y_i))
        return min_f

# Main function to solve the problem
def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, s = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        # Initialize dynamic programming table (3D array)
        dp = [[[float('inf')] * (s + 1) for _ in range(n)] for _ in range(s + 1)]
        # Populate dynamic programming table
        for i in range(1, n+1):
            for j in range(1, min(i, s)+1):
                if i == 1:
                    dp[j][0][j-1] = (s-j) * a[i]
                else:
                    for x_i in range(j+1):
                        y_i = a[i] - x_i
                        dp[j][i-1][x_i] = min(dp[j][i-1][x_i], dp[j-x_i][i-2][y_i])
        # Print the minimum possible value of F for the entire sequence
        print(min(dp[s][n-1]))

if __name__ == "__main__":
    main()
