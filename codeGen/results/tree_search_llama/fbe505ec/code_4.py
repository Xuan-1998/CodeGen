import re

# Read input from stdin
n = int(input())
words = []
for _ in range(n):
    word = input()
    words.append(word)

# Define regex pattern to match words longer than 10 characters
pattern = r'\b\w{11,}\b'

# Replace words longer than 10 characters with the abbreviation
for i, word in enumerate(words):
    if re.match(pattern, word):
        abbreviation = word[0] + str(len(word) - 2) + word[-1]
        print(abbreviation)
    else:
        print(word)

