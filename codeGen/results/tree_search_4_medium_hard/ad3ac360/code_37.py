def min_cuts(s):
    # Initialize memoization dictionary
    memo = {}

    def is_palindrome(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True

    def min_cuts_recursive(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if is_palindrome(i, j):
            # If the current substring is palindromic, no cuts are needed
            return 0
        else:
            # Find the minimum number of cuts needed to partition the string into palindrome substrings
            min_cuts = float('inf')
            for k in range(i, j + 1):
                if is_palindrome(i, k - 1) and is_palindrome(k + 1, j):
                    # Recursively call min_cuts_recursive on the left and right parts of the string
                    cuts_left = min_cuts_recursive(i, k - 1)
                    cuts_right = min_cuts_recursive(k + 1, j)

                    if cuts_left != -1 and cuts_right != -1:
                        # Update the minimum number of cuts needed
                        min_cuts = min(min_cuts, cuts_left + cuts_right + 1)
            return min_cuts

    return min_cuts(0, len(s) - 1)


# Test the function with a sample input
s = input()
print(min_cuts(s))
