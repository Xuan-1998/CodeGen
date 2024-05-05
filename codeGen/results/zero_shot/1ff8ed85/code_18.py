def can_send_over_network(b):
    # Convert b to a string for easier manipulation
    b_str = str(b)

    # Check if all elements in b are single-digit numbers (0-9)
    if not set(map(int, b_str)).issubset({i for i in range(10)}):
        return "NO"  # If not, it's impossible to obtain b from a

    # Initialize an empty list to store the segments of a
    a_segments = []

    # Iterate through the digits in b
    for digit in b_str:
        # Try to find a segment in a that matches this digit
        found = False
        for i, segment in enumerate(a_segments):
            if str(segment).endswith(digit):
                # If we find a match, remove the segment from the list and break
                del a_segments[i]
                found = True
                break

        # If we didn't find a matching segment, add it to the list
        if not found:
            a_segments.append(int(digit))

    # Check if the lengths of the segments in a match the original sequence b
    if a_segments != [len(str(segment)) for segment in a_segments]:
        return "NO"  # If they don't match, it's impossible to obtain b from a

    return "YES"  # If we reached this point, we can send b over the network!

t = int(input())  # Read the number of test cases
for _ in range(t):
    n = int(input())  # Read the size of the sequence b
    b = list(map(int, input().split()))  # Read the sequence b itself
    print(can_send_over_network(b))  # Print the result
