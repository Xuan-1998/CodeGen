def partition_palindromes(S):
    result = []
    def is_palindrome(s):
        return s == s[::-1]

    def partition_palindromes_helper(S, start_index, result):
        if start_index == len(S):
            result.append([S])
            return

        for end_index in range(start_index + 1, len(S) + 1):
            substring = S[start_index:end_index]
            if is_palindrome(substring):
                partition_palindromes_helper(S[end_index:], start_index, result)

    partition_palindromes_helper(S, 0, result)
    return result

# Example usage:
S = input()
result = partition_palindromes(S)
print(result)
