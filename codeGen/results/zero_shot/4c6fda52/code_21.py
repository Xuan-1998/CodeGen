import sys

def solve():
    n, k = map(int, input().split())
    s = input()
    
    # Initialize a set to store all possible substrings of length k
    substrings = set()
    for i in range(n - k + 1):
        substrings.add(s[i:i+k])
        
    # Initialize a variable to store the minimum number of characters that need to be changed
    min_changes = float('inf')
    
    # Iterate over each character in the string
    for i in range(n):
        # Create a copy of the original string
        new_s = list(s)
        
        # Replace the current character with 'R', 'G', or 'B'
        new_s[i] = 'R' if s[i] == 'G' else ('G' if s[i] == 'B' else 'B')
        
        # Convert the modified string into a set of substrings
        for j in range(n - k + 1):
            substrings.add(''.join(new_s[j:j+k]))
        
        # Count the number of characters that need to be changed
        changes = sum(1 for c1, c2 in zip(s, new_s) if c1 != c2)
        
        # Update the minimum number of characters that need to be changed
        min_changes = min(min_changes, changes)
    
    print(min_changes)

if __name__ == "__main__":
    solve()
