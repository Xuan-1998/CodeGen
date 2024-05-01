    # Initialize the top-left corner of the array as true (both 'A' appears after 'B', and neither 'AB' nor 'BA' has been found).
    prev_state = [(False, False) for _ in range(2)]

    for char in input().strip():
        if char == 'A':
            # Update the state based on whether we've seen 'B' before
            next_state = [(prev_state[1][0], True) if not prev_state[0][1] else prev_state[0]]
        elif char == 'B':
            # Update the state based on whether we've seen 'A' before
            next_state = [(not prev_state[0][0], prev_state[1][0])]

        # If we've found both 'AB' and 'BA', print "YES" and exit
        if all(state for state in next_state):
            print("YES")
            break

    else:
        print("NO")
