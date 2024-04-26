import sys

# Define the categories and their corresponding keywords
categories = {
    'IT': ['roma', 'rome'],
    'chemistry': ['maxim', 'maximum'],
    'design': ['dani', 'danik']
}

# Read the input string from stdin
input_string = sys.stdin.readline().strip()

# Iterate over each category and its keywords
for category, keywords in categories.items():
    # Check if any of the keywords are present in the input string
    for keyword in keywords:
        if keyword.lower() in input_string.lower():
            print(category)  # Print the matching category
            sys.exit(0)

print('Vlad')  # Default category is 'Vlad'
