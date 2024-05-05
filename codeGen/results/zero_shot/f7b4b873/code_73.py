def is_palindrome(s):
    return s == s[::-1]

def palindromic_partitions(S):
    def partition(S, partition):
        if not S:
            yield [partition]
        for i in range(1, len(S) + 1):
            if S[:i] == S[:i][::-1]:
                yield from partition(S[i:], partition + [S[:i]])

    return list(partition(S, []))

S = input()
print(palindromic_partitions(S))
