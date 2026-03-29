def partition_palindromes(s):
    def is_palindrome(s):
        return s == s[::-1]

    def partition_recursive(s, current_partition, result):
        if len(s) == 0:
            result.append(current_partition)
        else:
            for i in range(len(s)):
                if is_palindrome(s[:i+1]):
                    remaining_s = s[i+1:]
                    new_partition = [s[:i+1]] + current_partition
                    partition_recursive(remaining_s, new_partition, result)

    result = []
    partition_recursive(s, [], result)
    return result

# Test the function
S = input()
print(partition_palindromes(S))
