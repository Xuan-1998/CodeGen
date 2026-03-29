def min_function_value(n, s, sequence):
    # Step 1: Sort the sequence in descending order
    sorted_sequence = sorted((x for x in sequence), reverse=True)

    # Step 2: Initialize variables to store the minimum value and the current sum
    min_value = 0
    curr_sum = 0

    # Step 3: Iterate over the sorted sequence
    for i, a in enumerate(sorted_sequence):
        if i % 2 == 0:
            # If it's an even index, add the number to the current sum
            curr_sum += a - s
        else:
            # If it's an odd index, subtract the number from the current sum
            curr_sum -= a - s

        # Update the minimum value if the current sum is less than it
        min_value = max(min_value, curr_sum)

    return min_value
