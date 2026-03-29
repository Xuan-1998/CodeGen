def count_steady_tables(N, M):
    # Initialize the result variable
    result = 0

    # Loop through each row
    for i in range(N):
        # Initialize the current row sum and column pointer
        row_sum = 0
        col_ptr = 0

        # Loop through each element in the current row
        while col_ptr < M:
            # Add the current element to the row sum
            row_sum += (i + 1) % M

            # Move to the next column and check if the row sum has exceeded M
            if row_sum > M:
                break
            col_ptr += 1

        # If we reached the end of the row without exceeding M, increment the result
        if col_ptr == M:
            result = (result + 1) % 1000000000

    return result

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(count_steady_tables(N, M))
