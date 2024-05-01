import sys

def find_AB(s):
    n = len(s)
    A_idx = [i for i in range(n) if s[i] == 'A']
    B_idx = [i for i in range(n) if s[i] == 'B']

    # Create a dictionary to store the results of subproblems
    memo = {}

    def helper(i):
        if (i, 'AB') in memo:
            return memo[(i, 'AB')]
        if i >= len(s):
            return False

        # Check for "AB" or "BA"
        if s[i:i+2] in ['AB', 'BA']:
            remaining = s[i+2:]
            result = helper(i+2)  # Recursively check the remaining string
            memo[(i, 'AB')] = result
            return result

        # If no "AB" or "BA" found, move on to the next character
        return helper(i+1)

    # Start the dynamic programming process
    result = helper(0)
    if result:
        print("YES")
    else:
        print("NO")

# Read input from stdin
s = sys.stdin.readline().strip()

find_AB(s)
