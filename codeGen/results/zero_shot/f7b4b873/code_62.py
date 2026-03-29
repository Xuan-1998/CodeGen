def palindromic_partitions(s):
    def is_palindrome(s):
        return s == s[::-1]

    def recursive_partition(s, current_partition, result):
        if not s:  # base case: no more characters left in the string
            result.append(current_partition)
            return
        for i in range(1, len(s) + 1):  # consider all possible substrings
            substring = s[:i]
            if is_palindrome(substring):  # check if the substring is a palindrome
                recursive_partition(s[i:], current_partition + [substring], result)

    result = []
    recursive_partition(s, [], result)
    return result

# Example usage:
s = input()  # read the input string from stdin
result = palindromic_partitions(s)
print(result)  # print the list of palindromic partitions to stdout
