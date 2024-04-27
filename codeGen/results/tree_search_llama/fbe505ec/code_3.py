import sys

def solve():
    n = int(sys.stdin.readline())
    words = []
    
    for _ in range(n):
        word = sys.stdin.readline().strip()
        if len(word) > 10:
            abbreviation = word[0] + str(len(word)-2) + word[-1]
            words.append(abbreviation)
        else:
            words.append(word)
    
    for word in words:
        print(word)

solve()
