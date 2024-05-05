from collections import defaultdict

def solve(n, k, s):
    # Initialize a dictionary to store the count of 'R', 'G', and 'B' in the first i characters
    count = defaultdict(int)
    for c in s[:k]:
        count[c] += 1
    
    # The minimum number of changes needed is the difference between the counts of 'R' and 'G'
    min_changes = abs(count['R'] - count['G'])
    
    # Iterate over the rest of the string
    for i in range(k, n):
        # Update the counts based on the new character
        count[s[i-1]] -= 1
        count[s[i]] += 1
        
        # If the counts are equal, no changes are needed; otherwise, increment the minimum number of changes
        min_changes = min(min_changes, abs(count['R'] - count['G']))
    
    return min_changes

# Read input from standard input
n = int(input())
for _ in range(n):
    k = int(input())
    s = input()
    
    # Compute and print the minimum number of changes needed
    print(solve(k, n, s))
