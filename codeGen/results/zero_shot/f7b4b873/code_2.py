def is_palindrome(s):
    return s == s[::-1]

def palindromic_partitions(s):
    partitions = []
    
    def recursive_partition(s, partition):
        if not s:
            partitions.append(partition)
            return
        
        for i in range(len(s)):
            substring = s[:i+1]
            if is_palindrome(substring):
                recursive_partition(s[i+1:], partition + [substring])
    
    recursive_partition(input().strip(), [])
    
    print([list(map(str, p)) for p in partitions])
