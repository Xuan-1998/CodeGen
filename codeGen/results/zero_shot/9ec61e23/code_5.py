def calculate_mex_sum(n, top, bottom):
    # Initialize the sum of MEX values and the set of encountered pairs
    mex_sum = 0
    encountered_pairs = set()

    for i in range(n):
        # Create the current pair from top and bottom strings
        current_pair = (top[i], bottom[i])

        # If the current pair is (0,0) and not encountered before, it's a new bi-table
        if current_pair == ('0', '0') and current_pair not in encountered_pairs:
            mex_sum += 0  # MEX is 0 for this new bi-table
            encountered_pairs = {current_pair}  # Reset encountered pairs for the new bi-table

        # If the current pair is new and not (0,0), it increases the MEX of the current bi-table
        elif current_pair not in encountered_pairs:
            mex_sum += len(encountered_pairs)  # MEX is the size of encountered pairs
            encountered_pairs = {current_pair}  # Reset encountered pairs for the new bi-table

        # If the current pair is already encountered, just add it to the set
        else:
            encountered_pairs.add(current_pair)

    # Add the MEX of the last bi-table to the sum
    mex_sum += len(encountered_pairs)

    return mex_sum

# Read the number of test cases
t = int(input())
for _ in range(t):
    # Read the number of columns and the binary strings
    n = int(input())
    top = input().strip()
    bottom = input().strip()

    # Calculate and print the result
    result = calculate_mex_sum(n, top, bottom)
    print(result)
