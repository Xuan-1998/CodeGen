def palindromic_partitions(s):
    def is_palindrome(s):
        return s == s[::-1]

    def partition(s, current_partition=[]):
        if not s:
            result.append(current_partition)
            return
        for i in range(1, len(s) + 1):
            prefix = s[:i]
            suffix = s[i:]
            if is_palindrome(prefix + suffix):
                partition(suffix, current_partition + [prefix])
        return

    result = []
    partition(s)
    return result

s = input()
print(palindromic_partitions(s))
