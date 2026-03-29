def solve():
    n, q = map(int, input().split())
    signs = list(input())

    # Calculate the total sum of all 1's and -1's in the array.
    total_sum = sum(1 if sign == "+" else -1 for sign in signs)

    # Initialize variables to store the sums of 1's and -1's in the left half and right half of the array.
    left_sum, right_sum = 0, 0

    # Process each query.
    for _ in range(q):
        l, r = map(int, input().split())

        # Calculate the total sum of 1's and -1's in the current range.
        range_sum = sum(1 if signs[i] == "+" else -1 for i in range(l-1, r))

        # If the sign-variable sum of the range is non-zero, calculate how many elements we need to remove from the range.
        if total_sum != range_sum:
            if total_sum > 0 and range_sum < 0:
                left_sum = abs(range_sum)
            elif total_sum < 0 and range_sum > 0:
                right_sum = -abs(range_sum)

        # Print the minimum number of elements that can be removed from the current range.
        print(min(left_sum, right_sum))

if __name__ == "__main__":
    solve()
