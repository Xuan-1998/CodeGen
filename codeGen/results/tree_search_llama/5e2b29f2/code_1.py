def meme_category():
    keywords = {'roma': 'IT', 'maxim': 'chemistry', 'dani': 'design'}
    pattern = ''
    while True:
        line = input().lower()
        for keyword, category in keywords.items():
            if keyword in line and not pattern:
                pattern = keyword
                break
        if pattern:
            print(pattern)
            return

meme_category()
