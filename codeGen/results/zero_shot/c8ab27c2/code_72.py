s = input().strip()
t = input().strip()

def length_of_shortest_uncommon_subsequence():
    uncommon_subsequences = []
    
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            subsequence = s[i:j]
            
            if not is_subsequence(subsequence, t) and subsequence not in uncommon_subsequences:
                uncommon_subsequences.append(subsequence)
                
            if not uncommon_subsequences:
                return -1
    else:
        return min(map(len, uncommon_subsequences))

def is_subsequence(subsequence, string):
    for char in subsequence:
        if char not in string:
            return False
    
    return True

print(length_of_shortest_uncommon_subsequence())
