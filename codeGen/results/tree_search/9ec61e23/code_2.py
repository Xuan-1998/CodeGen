def calculate_mex(column):
    return 2 if column == ['00'] else 1 if '0' in column else 0

def solve(n, top_row, bottom_row):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        column = top_row[i-1] + bottom_row[i-1]
        mex = calculate_mex(column)
        if mex == 2 and calculate_mex(top_row[i-2] + bottom_row[i-2]) == 2:
            dp[i] = dp[i - 1]
        else:
            dp[i] = dp[i - 1] + mex
    return dp[n]

def main():
    t = int(input().strip())  # Number of test cases
    for _ in range(t):
        n = int(input().strip())  # Number of columns in the bi-table
        top_row = input().strip()  # Top row of the bi-table
        bottom_row = input().strip()  # Bottom row of the bi-table
        result = solve(n, top_row, bottom_row)
        print(result)

if __name__ == "__main__":
    main()
