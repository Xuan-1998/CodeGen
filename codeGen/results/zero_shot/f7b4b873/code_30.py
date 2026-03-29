def palindromic_partitions(S):
    result = []
    def partition(s):
        if len(s) == 0:
            return [[]]
        partitions = []
        for i in range(1, len(s)):
            if s[:i] == s[:i][::-1]:
                partitions += [[s[:i]]] + partition(s[i:])
        return partitions
    result = partition(S)
    return result

S = input()
print(palindromic_partitions(S))
