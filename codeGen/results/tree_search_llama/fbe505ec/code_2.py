import sys

def replace_long_words():
    n = int(input())
    
    for _ in range(n):
        word = input()
        
        if len(word) > 10:
            abbreviation = word[0] + str(len(word) - 2) + word[-1]
            print(abbreviation)
        else:
            print(word)

replace_long_words()
