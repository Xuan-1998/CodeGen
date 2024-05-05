def palindromic_partitions(S):
    def is_palindrome(s):
        return s == s[::-1]

    def partition(S):
        if len(S) == 0:
            return [[]]
        partitions = []
        for i in range(1, len(S) + 1):
            if is_palindrome(S[:i]):
                for p in partition(S[i:]):
                    partitions.append([S[:i]] + p)
        return partitions

    result = partition(S)
    return [' '.join(map(str, p)) for p in result]

if __name__ == "__main__":
    S = input()
    print(*palindromic_partitions(S), sep='\n')
