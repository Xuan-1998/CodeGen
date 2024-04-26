def count_bear_substrings(s):
    # Initialize counter variable
    bear_count = 0

    # Iterate over the input string with a sliding window of length 4 (since 'bear' has 4 characters)
    for i in range(len(s) - 3):  # -3 because we need 4 characters to match 'bear'
        # Check if the current substring matches 'bear'
        if s[i:i+4] == 'bear':
            bear_count += 1

    return bear_count


if __name__ == "__main__":
    s = input()
    print(count_bear_substrings(s))
