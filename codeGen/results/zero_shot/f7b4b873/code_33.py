def palindrome_partition(s):
    def helper(s, i):
        if not s or i == len(s):
            return []
        
        result = []
        for j in range(i + 1, len(s) + 1):
            if s[i:j] == s[i:j][::-1]:
                result.extend(helper(s[:i], 0))
                result.append([s[i:j]])
        return result
    
    return helper(s, 0)

# Example usage
input_string = input()
result = palindrome_partition(input_string)
print(result)
