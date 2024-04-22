def calculate_mex(segment):
    # Since there are only four possible pairs of bits, we can hardcode their MEX values
    mex_values = {'00': 2, '01': 2, '10': 2, '11': 3}
    for pair in ['00', '01', '10']:
        if pair not in segment:
            return mex_values[pair]
    return mex_values['11']

def solve(n, top_row, bottom_row):
    dp = [0] * (n + 1)
    max_mex = 0
    last_cut = 0

    for i in range(1, n):
        if top_row[i] != top_row[i - 1] or bottom_row[i] != bottom_row[i - 1]:
            segment = top_row[last_cut:i] + ' ' + bottom_row[last_cut:i]
            max_mex += calculate_mex(segment)
            last_cut = i

    # Add MEX for the last segment
    segment = top_row[last_cut:n] + ' ' + bottom_row[last_cut:n]
    max_mex += calculate_mex(segment)

    dp[n] = max_mex
    return dp[n]

def main():
    t = int(input().strip())  # Number of test cases
    for _ in range(t):
        n = int(input().strip())  # Number of columns in the bi-table
        top_row = input().strip()
        bottom_row = input().strip()
        result = solve(n, top_row, bottom_row)
        print(result)

if __name__ == "__main__":
    main()
