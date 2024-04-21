import sys

def max_sum_of_smallest_missing_digit(test_cases):
    results = []
    for n, row1, row2 in test_cases:
        result = 0
        i = 0
        while i < n:
            # If both rows have the same digit at column i
            if row1[i] == row2[i]:
                # If the digit is 0, the smallest missing digit is 1
                if row1[i] == '0':
                    result += 1
                # Move to the next column
                i += 1
            else:
                # If the digits are different, the smallest missing digit is 2
                result += 2
                # Skip the next column as well since we've already counted this pair
                i += 2
        results.append(result)
    return results

def main():
    # Reading the number of test cases
    t = int(sys.stdin.readline().strip())
    test_cases = []
    for _ in range(t):
        # Reading the number of columns for each test case
        n = int(sys.stdin.readline().strip())
        # Reading the two rows of the bi-table
        row1 = sys.stdin.readline().strip()
        row2 = sys.stdin.readline().strip()
        test_cases.append((n, row1, row2))
    
    # Calculate and output the results
    results = max_sum_of_smallest_missing_digit(test_cases)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
