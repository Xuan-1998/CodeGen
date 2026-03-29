def palindrome_partitions(s):
    memo = {}

    def helper(i, path=[]):
        if i == len(s):
            return [path]
        
        result = []
        
        for j in range(i + 1, len(s) + 1):
            if s[i:j] == s[i:j][::-1]:
                new_path = path + [s[i:j]]
                
                if i == 0:
                    result.append(new_path)
                else:
                    partitions = helper(i - 1, new_path)
                    for p in partitions:
                        result.extend([p + [s[i:j]]])
                    
        return result
        
    return memo.get(len(s), []) or helper(len(s))

# Test the function
input_string = input()
output = palindrome_partitions(input_string)

for partition in output:
    print(partition)
