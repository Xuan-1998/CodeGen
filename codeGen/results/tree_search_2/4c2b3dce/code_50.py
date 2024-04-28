# Take input from stdin
s = input()

# Count the occurrences of 'A' and 'B'
a_count = s.count('A')
b_count = s.count('B')

if (a_count - b_count) % 2 == 0 or (b_count - a_count) % 2 == 0:
    print("YES")
else:
    print("NO")
