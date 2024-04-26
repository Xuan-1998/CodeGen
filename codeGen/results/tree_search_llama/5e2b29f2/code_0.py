def categorize_meme(meme):
    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword.lower() in meme.lower():
                return f'Vlad'  # default to 'other'
        else:
            return category

# Example usage:
meme = input()
print(categorize_meme(meme))
