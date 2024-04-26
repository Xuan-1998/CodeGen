def can_flip_to_palindrome():
    N = int(input())
    S = input()

    # Reverse the string for easy comparison
    T = S[::-1]

    # Initialize a counter for mismatched pairs
    mismatches = 0

    # Iterate over the characters in the original and reversed strings
    for i in range(N):
        if S[i] != T[i]:
            # If we find a mismatch, increment the counter
            mismatches += 1
        elif S[i] == '1' and T[i] == '0':
            # If the pair is different but can be flipped to match, decrement the counter
            mismatches -= 1

    # Return YES if there are an even number of mismatches (can flip to palindrome), NO otherwise
    return 'YES' if mismatches % 2 == 0 else 'NO'

print(can_flip_to_palindrome())
