def partition_palindromes(S):
    def is_palindrome(s):
        return s == s[::-1]

    partitions = []
    for i in range(len(S)):
        for j in range(i + 1, len(S) + 1):
            substr = S[i:j]
            if is_palindrome(substr):
                partitions.append([substr])
    
    # Find all possible palindromic partitions
    for i in range(len(partitions)):
        for j in range(i + 1, len(partitions)):
            partition = partitions[i] + partitions[j]
            if is_palindrome(''.join(partition)):
                partitions.append(partition)
    
    return partitions

S = input()
print(partition_palindromes(S))
