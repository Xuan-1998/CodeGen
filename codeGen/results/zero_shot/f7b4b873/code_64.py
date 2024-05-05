def partition_palindromes(s):
    def is_palindrome(s):
        return s == s[::-1]

    result = []
    for i in range(1, len(s)):
        for j in range(i, 0, -1):
            if is_palindrome(s[j:i+1]):
                result.append([s[:j], s[j:i+1], s[i:]])
    return result

input_string = input()
print(partition_palindromes(input_string))
