import re

def get_category(meme):
    categories = {
        'roma': ['it', 'information technology'],
        'maxim': ['chemistry'],
        'danik': ['design']
    }

    for category, keywords in categories.items():
        for keyword in keywords:
            if re.search(r'\b' + re.escape(keyword) + r'\b', meme, flags=re.IGNORECASE):
                return category

    return 'Vlad'

meme = input()
print(get_category(meme))
