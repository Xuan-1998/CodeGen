def calculate_mex_sum(n, row1, row2):
    seen = set()
    mex_sum = 0

    for i in range(n):
        # Convert the two bits into a number and add it to the set
        num = int(row1[i]) * 2 + int(row2[i])
        seen.add(num)

        # If we have seen all numbers, we can split here and start a new bi-table
        if len(seen) == 4:
            mex_sum += 4
            seen.clear()

    # Add the MEX of the last sequence if it's not empty
    if seen:
        # The MEX is the smallest number not in the set, which can be from 0 to 3
        for mex in range(4):
            if mex not in seen:
                mex_sum += mex
                break

    return mex_sum

def main():
    t = int(input().strip())  # Read the number of test cases
    for _ in range(t):
        n = int(input().strip())  # Read the number of columns
        row1 = input().strip()  # Read the first row
        row2 = input().strip()  # Read the second row
        print(calculate_mex_sum(n, row1, row2))

if __name__ == "__main__":
    main()
