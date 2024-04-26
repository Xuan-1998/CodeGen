import re

def categorize_meme(meme):
    categories = {
        'IT': r' Roma|rome|rmi',
        'chemistry': r'maxim|max|chemical|chem',
        'design': r'danik|danik|designer',
        'other': '.*'
    }

    for category, pattern in categories.items():
        if re.search(pattern, meme, re.IGNORECASE):
            return category

    return 'other'

if __name__ == '__main__':
    meme = input().strip()
    print(categorize_meme(meme))
