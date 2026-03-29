import sys

def count_words(n, m):
    # Initialize the number of possible words to 1 (the empty word)
    total_words = 1
    
    for i in range(m):
        if i % n < n // 2:
            # For letters at indices less than half the size of the alphabet,
            # we can place them anywhere in the word
            total_words *= (n - i % n)
        else:
            # For letters at indices greater than or equal to half the size of the alphabet,
            # we can only place them as the last letter or immediately followed by any letter
            total_words *= (2 * n - i % n)
    
    return total_words % (10**8 + 7)

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    print(count_words(n, m))
