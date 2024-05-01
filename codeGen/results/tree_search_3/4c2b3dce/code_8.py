code = input()

# Initialize the 2D table
table = [[False for _ in range(3)] for _ in range(len(code))]

# Fill the table
for i in range(len(code)):
    if code[i:i+2] == "AB":
        table[i][0] = True
    elif code[i:i+2] == "BA" and i > 0:
        table[i-1][1] = True

# Check for the presence of 'AB' and 'BA' substrings
found_AB = False
found_BA = False
for i in range(len(code)):
    if table[i][0]:
        found_AB = True
    if table[i][1]:
        found_BA = True

# Print the result
if found_AB and found_BA:
    print("YES")
else:
    print("NO")
