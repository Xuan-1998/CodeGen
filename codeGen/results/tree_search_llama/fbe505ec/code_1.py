def solve(input_words):
    output_words = []
    for word in input_words:
        if len(word) > 10:
            # Calculate the special abbreviation
            first_letter = word[0]
            last_letter = word[-1]
            num_letters = len(word) - 2
            abbreviation = f"{first_letter}{num_letters}{last_letter}"
            output_words.append(abbreviation)
        else:
            output_words.append(word)
    return output_words

# Read input from stdin
n = int(input())
input_words = [input() for _ in range(n)]

# Calculate and print the output
output_words = solve(input_words)
for word in output_words:
    print(word)
