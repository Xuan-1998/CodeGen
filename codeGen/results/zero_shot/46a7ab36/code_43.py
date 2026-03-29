def count_words(n, m):
    # Initialize the result variable
    result = 1

    # Iterate over each position in the word
    for i in range(m):
        # If this is the last character or it's not possible to place this letter,
        # then we can only choose from the remaining letters (n-1)
        if i == m - 1 or 2 * i > n:
            result = (result * (n - i)) % (10**8 + 7)
        else:
            # Otherwise, we have n possibilities for this character
            result = (result * n) % (10**8 + 7)

    return result

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(count_words(n, m))
