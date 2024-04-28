def longest_palindromic_substring(s):
    palindromes = {}
    for i, c in enumerate(s):
        if c not in palindromes:
            for j in range(i + 1):
                palindrome = s[j:i+1]
                if palindrome == palindrome[::-1]:
                    palindromes[c] = palindrome
                    break
    max_length = max(len(palindrome) for palindrome in palindromes.values())
    return max((palindrome for palindrome, length in palindromes.items() if length == max_length), default='')

# Example usage:
s = input()
print(longest_palindromic_substring(s))
