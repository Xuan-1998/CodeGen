def calculate_mex(s1, s2):
    if s1 == s2 == '1':
        return 0
    elif s1 == '0' and s2 == '0':
        return 0
    else:
        return 1

def solve(n, top_row, bottom_row):
    total_mex = 0
    current_mex = calculate_mex(top_row[0], bottom_row[0])

    for i in range(1, n):
        if top_row[i] == bottom_row[i] == '1':
            total_mex += current_mex
            current_mex = 0
        else:
            new_mex = calculate_mex(top_row[i], bottom_row[i])
            if new_mex == 1 and current_mex == 1:
                total_mex += current_mex
                current_mex = new_mex
            else:
                current_mex = max(current_mex, new_mex)

    total_mex += current_mex
    return total_mex

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
