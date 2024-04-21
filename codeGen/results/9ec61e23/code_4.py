import sys

def mex_sum(binary_strings):
    top, bottom = binary_strings
    n = len(top)
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if top[i - 1] != bottom[i - 1]:  # Column has mixed 0s and 1s
            dp[i] = dp[i - 1] + 2
        else:  # Column has only 0s or only 1s
            # If previous column has mixed 0s and 1s, start a new segment
            if i > 1 and top[i - 2] != bottom[i - 2]:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = dp[i - 1] + 1  # Continue the previous segment
    
    return dp[n]

def main():
    t = int(sys.stdin.readline().strip())  # Read number of test cases
    for _ in range(t):
        n = int(sys.stdin.readline().strip())  # Read number of columns
        top_row = sys.stdin.readline().strip()  # Read top row of bi-table
        bottom_row = sys.stdin.readline().strip()  # Read bottom row of bi-table
        result = mex_sum((top_row, bottom_row))
        print(result)

if __name__ == "__main__":
    main()
