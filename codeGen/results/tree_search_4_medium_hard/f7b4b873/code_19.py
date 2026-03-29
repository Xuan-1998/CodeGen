def find_palindromic_partitions(s):
    memo = {}
    def helper(i, j, partition):
        if (i, j) in memo:
            return memo[(i, j)]
        if i > j:
            return [partition]
        
        # check for palindrome
        if s[i] == s[j]:
            new_partition = partition + [s[i:j+1]]
            result = helper(i+1, j, new_partition)
            result.append([partition])
            memo[(i, j)] = result
            return result
        
        # no palindrome found
        left_result = helper(i+1, j, partition)
        right_result = helper(i, j-1, partition)
        results = left_result + right_result
        memo[(i, j)] = results
        return results
    
    result = helper(0, len(s)-1, [])
    return result

# test the function
s = input()
print(find_palindromic_partitions(s))
