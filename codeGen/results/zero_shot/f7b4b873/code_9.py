def find_palindromic_partitions(S):
    n = len(S)
    partitions = []
    
    def is_palindrome(i, j):
        while i < j:
            if S[i] != S[j]:
                return False
            i += 1
            j -= 1
        return True
    
    def backtrack(start, partition):
        if start == n:
            partitions.append(list(partition))
            return
        
        for end in range(start, n):
            if is_palindrome(start, end):
                partition.append(S[start:end+1])
                backtrack(end+1, partition)
                partition.pop()
    
    backtrack(0, [])
    return partitions

S = input()
partitions = find_palindromic_partitions(S)
for p in partitions:
    print(p)

