import sys

def preprocess_string(s):
    # Construct suffix array using Rabin-Karp algorithm
    n = len(s)
    suffix_array = [s[i:] for i in range(n)]
    return sorted(suffix_array)

def common_substrings(str1, str2):
    N = len(str1)
    NA = len(str2)
    
    # Preprocess strings to get suffix arrays
    suffix_array1 = preprocess_string(str1)
    suffix_array2 = preprocess_string(str2)
    
    max_common = 0
    
    for i in range(N):
        for j in range(NA):
            substring = str1[i:i+min(N-1, NA-j)]
            
            # Check if substring is present in both arrays
            if substring in suffix_array1 and substring in suffix_array2:
                last_occurrence1 = -1
                last_occurrence2 = -1
                
                for k in range(len(suffix_array1)):
                    if suffix_array1[k].startswith(substring):
                        last_occurrence1 = k
                    elif suffix_array2[k].startswith(substring):
                        last_occurrence2 = k
                        
                    # Break loop once we've found the maximum common substring
                    if last_occurrence1 >= 0 and last_occurrence2 >= 0:
                        max_common += 1
                        break
                
    return max_common

# Read input strings from standard input
str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()

# Calculate the maximum number of common non-overlapping substrings
max_common = common_substrings(str1, str2)

print(max_common)
