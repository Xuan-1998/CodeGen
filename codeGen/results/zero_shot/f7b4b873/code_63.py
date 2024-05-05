def palindromic_partitions(s):
    def is_palindrome(s):
        return s == s[::-1]

    result = []
    for i in range(1, len(s) + 1):
        for j in range(i, len(s) + 1):
            partition = s[i - 1:j]
            if is_palindrome(partition):
                result.append([partition])
    
    return [''.join(p).split(' ') for p in set(map(' '.join, result))]

s = input()
print(palindromic_partitions(s))
