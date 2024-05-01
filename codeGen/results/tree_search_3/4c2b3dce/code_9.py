# Read the input from stdin
s = input()

# Check if 'AB' appears before 'BA'
if s.find('AB') != -1 and (s.find('BA', s.find('AB')+2) != -1 or s.find('BA', 0, s.find('AB')) != -1):
    print("YES")
else:
    print("NO")
