def _partition(S, start, end, partitions):
    if start >= end:
        # If we've reached the end of the string, add the current partition to the list
        partitions.append(list(S[start:end+1]))
        return

    for i in range(start, end+1):
        # Consider each character as a potential starting point for a palindromic partition
        if S[i] == S[start]:  # Check if the characters are the same (for palindrome)
            _partition(S, start+1, i, partitions)  # Recursively explore the left side
            _partition(S, i+1, end, partitions)  # Recursively explore the right side

def palindromic_partitions(S):
    partitions = []
    _partition(S, 0, len(S)-1, partitions)
    return partitions

# Receive input from stdin
S = input()

# Call the function and print the result to stdout
print(palindromic_partitions(S))
