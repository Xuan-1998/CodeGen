def generate_all_possible_words(n, m):
    total = 1
    for i in range(m):
        total *= calculate_possible_letters(i)
    return total % (10**8 + 7)

# Get input from stdin
n, m = map(int, input().split())

# Calculate the number of possible words
total = generate_all_possible_words(n, m)

# Print the result to stdout
print(total)
