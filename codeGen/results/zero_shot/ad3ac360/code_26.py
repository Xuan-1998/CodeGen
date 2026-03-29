def min_cuts(s):
    n = len(s)
    cuts = 0

    for i in range(n):
        left, right = i, n-1
        while left <= right:
            if s[left:right+1] != s[left:right+1][::-1]:
                cuts += 1
                break
            left += 1
            right -= 1

    return cuts + 1

# Read input from standard input
s = input()

# Calculate the minimum number of cuts and print it to standard output
print(min_cuts(s))
