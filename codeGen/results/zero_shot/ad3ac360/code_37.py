def min_cuts(s):
    n = len(s)
    cuts = 0
    for i in range(n):
        if not is_palindrome(s, 0, i):  # check if substring up to i is a palindrome
            cuts += 1
    return cuts + (n - 1)  # add the last cut (if needed)

print(min_cuts(s))
