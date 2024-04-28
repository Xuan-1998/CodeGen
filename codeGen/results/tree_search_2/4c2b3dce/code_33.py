import sys

def solve():
    s = input().strip()
    
    # Count the frequency of each character
    a_count, b_count = 0, 0
    for c in s:
        if c == 'A':
            a_count += 1
        elif c == 'B':
            b_count += 1
    
    # Determine which substring comes first
    if a_count > b_count:
        first_occurrence = 'A'
    else:
        first_occurrence = 'B'
    
    # Check if the remaining part of the string contains the other substring
    if (a_count - b_count) % 2 == 1 and s.index(first_occurrence) + 1 < len(s):
        print("YES")
    elif (b_count - a_count) % 2 == 1 and s.index(first_occurrence) > 0:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()
