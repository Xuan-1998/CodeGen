def max_common_substrings(str1, str2):
    N = len(str1)
    common_substrs = set()
    
    # Initialize sliding window
    i = j = 0
    
    while i < N and j < N:
        # Create a substring of length k
        k = min(N - i, N - j)
        
        # Check if the substring is common between str1 and str2
        substr = str1[i:i+k]
        if substr in str2[j:j+k]:
            common_substrs.add(substr)
            i += k
            j += k
        else:
            i += 1
            j += 1
    
    return len(common_substrs)

# Read input from stdin
str1 = input().strip()
str2 = input().strip()

print(max_common_substrings(str1, str2))
