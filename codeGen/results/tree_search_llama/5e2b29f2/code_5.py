import re

def categorize_meme(meme_string):
    # Define the categories with their corresponding regex patterns
    categories = {
        'IT': r'(rome|roma)[\s\w]*',
        'Chemistry': r'(maxim|ma[xz])[\s\w]*',
        'Design': r'(dani|danik)[\s\w]*',
        'Other': r'[^a-z]+'
    }

    # Iterate through the categories and check if any pattern matches
    for category, pattern in categories.items():
        if re.search(pattern, meme_string, re.IGNORECASE):
            return category

    # If no match is found, return 'Other'
    return 'Other'

# Read the input from standard input
meme_string = input()

# Categorize and print the result
print(categorize_meme(meme_string))
