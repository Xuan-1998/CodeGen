import sys
from collections import Counter

def solve():
    n, k = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().strip()
    
    # Count the occurrences of each character in the original string
    counter = Counter(s)
    
    # Initialize the minimum number of changes needed
    min_changes = 0
    
    # Iterate through the characters and calculate the minimum number of changes needed
    for char in "RGB":
        count = counter[char]
        if count < k // 3:
            min_changes += (k // 3 - count) * 3
        elif count > k // 3:
            min_changes += (count - k // 3) * 3
    
    print(min_changes)

solve()
