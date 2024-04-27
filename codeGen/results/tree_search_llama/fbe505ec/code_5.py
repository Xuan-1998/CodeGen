import re

while True:
    try:
        word = input()
        if len(word) > 10:
            abbrev = word[0] + word[-1] + str(len(word) - 2)
            print(abbrev)
        else:
            print(word)
    except EOFError:
        break
