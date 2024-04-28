from collections import defaultdict

def solve(str1, str2):
    # Preprocess the strings by building suffix trees (or arrays)
    # This is an O(N) operation where N is the length of each string
    
    dp = defaultdict(int)
    last_occurrence = {}
    
    for i in range(len(str1)):
        for j in range(i + 1, len(str1) + 1):
            substring1 = str1[i:j]
            
            for k in range(len(str2)):
                for l in range(k + 1, len(str2) + 1):
                    substring2 = str2[k:l]
                    
                    # Check if the two substrings share any common characters
                    if all(c1 == c2 for c1, c2 in zip(substring1, substring2)):
                        # If they do, increment the count and update the last occurrence
                        if (substring1, substring2) not in dp:
                            dp[(substring1, substring2)] = 0
                        
                        dp[(substring1, substring2)] += 1
                        if c1 not in last_occurrence:
                            last_occurrence[c1] = i
                        if c2 not in last_occurrence:
                            last_occurrence[c2] = k
    
    # Return the maximum count of common non-overlapping substrings
    return max(dp.values())

# Example usage:
str1, str2 = input().split()
print(solve(str1, str2))
