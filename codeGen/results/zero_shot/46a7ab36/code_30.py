import sys

def count_words(n, m):
    # Calculate the base case: if i is greater than or equal to n/2, then we have two choices
    base_case = 1 << (m.bit_length() - 1)

    # Initialize the total number of possible words
    total_words = 0

    for i in range(1, m + 1):
        if 2 * i <= n:
            total_words += base_case
        else:
            total_words += 2 ** (i - 1)
    return total_words % (10**8 + 7)

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    print(count_words(n, m))
