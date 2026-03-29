def find_smallest_string(n, k):
    memo = {}
    
    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if j == 0:
            result = ""
        elif i > j:
            result = dp(n, k-j+1)
        else:
            delete = dp(i-1, j-1)
            duplicate = dp(n, k-j+1)
            
            if delete <= duplicate:
                result = delete
            else:
                result = duplicate
        
        memo[(i, j)] = result
        return result
    
    return dp(n, k).ljust(k)[0:k]

# Read input from stdin and print the output to stdout.
n, k = map(int, input().split())
print(find_smallest_string(n, k))
