def all_palindromic_partitions(S):
    def is_palindrome(s):
        return s == s[::-1]

    partitions = [[]]
    for char in S:
        new_partitions = []
        for p in partitions:
            new_partitions.append(p + [char])
            if p and p[-1] == char:
                new_partitions.append(p + [char, char])
        partitions = new_partitions

    palindromic_partitions = []
    for p in partitions:
        if is_palindrome(''.join(map(str, p))):
            palindromic_partitions.append(p)

    return palindromic_partitions

S = input()
print(all_palindromic_partitions(S))
