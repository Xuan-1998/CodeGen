===BEGIN SOLUTION===
from sys import stdin

# Read the input string from standard input
s = stdin.readline().strip()

# Count the occurrences of 'A' and 'B'
a_count = s.count('A')
b_count = s.count('B')

if a_count >= 1 and b_count >= 1:
    # Check for 'AB' substring using a sliding window approach
    ab_window = 0
    while ab_window < len(s) - 1:
        if s[ab_window:ab_window + 2] == 'AB':
            remaining_chars = len(s) - ab_window - 2
            if remaining_chars >= 2:  # Check for at least 2 more characters left
                # Start looking for 'BA' substring using a sliding window approach
                ba_window = 0
                while ba_window < remaining_chars - 1:
                    if s[ab_window + 2:ab_window + 4] == 'BA':
                        print("YES")
                        exit(0)
                    ba_window += 1
        ab_window += 1

print("NO")

===END SOLUTION===
