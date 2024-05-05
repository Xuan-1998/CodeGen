def is_palindrome(s):
    return s == s[::-1]

def find_partitions(S):
    N = len(S)
    partitions = []
    
    def recursive_partition(i, path):
        if i >= N:
            partitions.append(path)
            return
        
        for j in range(i + 1, N + 1):
            substring = S[i:j]
            if is_palindrome(substring):
                recursive_partition(j, [substring] + path)
                
    recursive_partition(0, [])
    return partitions

S = input()
print(find_partitions(S))
