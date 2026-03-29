import sys
def count_matrices(n):
    # Define the possible values for each element of the 2x2 matrix
    elements = [1, -1, 0]

    # Initialize the count of positive invertible matrices with trace N and determinant greater than 0
    count = 0

    # Iterate over all possible combinations of elements for the top-left and bottom-right corners of the matrix
    for a in elements:
        for d in elements:
            # Calculate the middle element of the matrix based on its trace and determinant
            b = (n - a) // 2
            c = n - a - 2*b

            # Check if the calculated values are valid (i.e., they form a 2x2 integer matrix with non-negative elements)
            if b >= 0 and c >= 0:
                # Calculate the determinant of the current matrix configuration
                det = a*c + b*d

                # If the determinant is positive, increment the count of matrices that meet the conditions
                if det > 0:
                    count += 1

    return count

# Read the number of test cases from stdin
T = int(sys.stdin.readline())

# Read the trace values for each test case and count the corresponding matrices
for _ in range(T):
    n = int(sys.stdin.readline())
    print(count_matrices(n))
