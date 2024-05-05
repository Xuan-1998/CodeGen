def count_ones(n):
    # Initialize the memo dictionary
    memo = {0: 0}

    for i in range(1, n + 1):
        # If the current number ends with 1, add 1 to the count of the previous number
        if i % 10 == 1:
            memo[i] = memo.get(i - 1, 0) + 1
        else:
            # If the current number does not end with 1, calculate its count based on the previous counts
            memo[i] = memo.get(i - 1, 0)

    return sum(memo.values())
