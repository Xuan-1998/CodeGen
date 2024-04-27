from typing import List

def count_bear_pairs(s: str) -> int:
    # Initialize a list to store the start and end indices of each occurrence of 'bear'
    bear_indices: List[tuple] = []

    # Iterate through the input string s
    i = 0
    while i < len(s):
        # Check if the substring from index i to i+4 (inclusive) is equal to 'bear'
        if s[i:i+4] == 'bear':
            # If it is, append the start and end indices of this occurrence to the list
            bear_indices.append((i, i+3))

            # Increment i by 1 to skip over the current 'bear' substring
            i += 4
        else:
            # If not, increment i by 1 to move on to the next character
            i += 1

    # Initialize a counter for the number of pairs where these occurrences overlap with each other
    pairs = 0

    # Iterate through the list of bear indices
    for i in range(len(bear_indices)):
        for j in range(i+1, len(bear_indices)):
            # Check if the current occurrence overlaps with the next one
            if bear_indices[i][1] >= bear_indices[j][0]:
                pairs += 1

    return pairs

