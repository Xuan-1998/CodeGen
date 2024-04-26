import re

def categorize_meme(meme):
    if re.search(r'roma|romaa', meme.lower()):
        return 'Roma'
    elif re.search(r'maxim|maxims', meme.lower()):
        return 'Maxim'
    elif re.search(r'danik|daniks', meme.lower()):
        return 'Danik'
    else:
        return 'Vlad'

if __name__ == "__main__":
    meme = input()
    print(categorize_meme(meme))
