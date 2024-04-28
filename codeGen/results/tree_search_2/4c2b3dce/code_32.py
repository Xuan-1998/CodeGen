from collections import defaultdict

def solve():
    # Read input from stdin
    s = input().strip()

    # Create a frequency map for 'A' and 'B'
    freq_map = defaultdict(int)
    for char in s:
        if char == 'A':
            freq_map['A'] += 1
        elif char == 'B':
            freq_map['B'] += 1

    # Check if one appears more frequently than the other
    a_freq, b_freq = freq_map['A'], freq_map['B']
    if a_freq > b_freq:
        # If 'A' is more frequent, check for substring 'BA'
        if s[a_freq:].count('B') >= 1 and s[a_freq:].count('A') >= 1:
            print("YES")
        else:
            print("NO")
    elif b_freq > a_freq:
        # If 'B' is more frequent, check for substring 'AB'
        if s[b_freq:].count('A') >= 1 and s[b_freq:].count('B') >= 1:
            print("YES")
        else:
            print("NO")
    else:
        # If both appear with the same frequency, we can't determine
        print("NO")

if __name__ == "__main__":
    solve()
