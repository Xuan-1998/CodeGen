def find_palindromic_partitions(S):
    def backtrack(start, path):
        if start == len(S):
            result.append(path)
            return
        
        for end in range(start, len(S)):
            if S[start:end+1] == S[start:end+1][::-1]:
                backtrack(end+1, path + [S[start:end+1]])
    
    result = []
    backtrack(0, [])
    return result

# Receive input from stdin
S = input()

# Call the function and print the output to stdout
print(find_palindromic_partitions(S))
