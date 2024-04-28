from collections import defaultdict

def longest_palindromic_substring(S):
    # Initialize the dictionary for memoization
    dp = defaultdict(str)

    def expand_around_center(left, right):
        while left >= 0 and right < len(S) and S[left] == S[right]:
            dp[(left, right)] = S[left:right+1]
            left -= 1
            right += 1

    for i in range(len(S)):
        # Consider even-length palindromes
        expand_around_center(i, i)
        # Consider odd-length palindromes
        expand_around_center(i, i + 1)

    max_length = 0
    longest_palindrome = ""
    for (left, right), palindrome in dp.items():
        if len(palindrome) > max_length:
            max_length = len(palindrome)
            longest_palindrome = palindrome

    return longest_palindrome


if __name__ == "__main__":
    S = input().strip()
    print(longest_palindromic_substring(S))
