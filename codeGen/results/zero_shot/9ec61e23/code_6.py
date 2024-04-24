def calculate_mex_sum(n, top_row, bottom_row):
    mex_sum = 0
    current_mex = 2  # Initially assume the MEX is 2, as it's the highest possible MEX for a bi-table

    for i in range(n):
        if top_row[i] == '0' and bottom_row[i] == '0':
            # If we encounter '00', we add the current MEX to the sum and reset the MEX to 0
            mex_sum += current_mex
            current_mex = 0
        elif top_row[i] == '1' and bottom_row[i] == '1':
            # If we encounter '11', and the current MEX is 0 or 1, we need to start a new bi-table
            if current_mex < 2:
                mex_sum += current_mex
                current_mex = 2
        else:
            # For '01' or '10', the MEX is at least 1
            current_mex = max(current_mex, 1)

    # Add the MEX of the last bi-table to the sum
    mex_sum += current_mex
    return mex_sum

def main():
    t = int(input().strip())  # Read the number of test cases
    for _ in range(t):
        n = int(input().strip())  # Read the number of columns in the bi-table
        top_row = input().strip()  # Read the top row of the bi-table
        bottom_row = input().strip()  # Read the bottom row of the bi-table
        print(calculate_mex_sum(n, top_row, bottom_row))

if __name__ == "__main__":
    main()
