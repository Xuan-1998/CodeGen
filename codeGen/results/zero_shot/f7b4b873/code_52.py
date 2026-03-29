def is_palindrome(s):
    return s == s[::-1]

def partition(s, current_partition=None):
    if current_partition is None:
        current_partition = []
    
    partitions = [current_partition]
    
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substring = s[i:j]
            
            if is_palindrome(substring):
                new_partition = current_partition + [substring]
                
                partitions.append(new_partition)
                
                partition(s[j:], new_partition)

    return partitions

# Read input from stdin
s = input()

# Generate and print all possible palindromic partitions
partitions = partition(s)
for p in partitions:
    print(p)
