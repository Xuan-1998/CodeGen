def find_palindromic_partitions(S):
    partitions = []
    def partition(i, s):
        if i >= len(S):
            partitions.append([s])
            return
        
        for j in range(i, len(S)):
            if S[i:j+1] == S[i:j+1][::-1]:
                partition(j+1, s + [S[i:j+1]])
    
    partition(0, [])
    return partitions

# Read the input string from stdin
S = input()

# Call the function and print the result to stdout
print(find_palindromic_partitions(S))
