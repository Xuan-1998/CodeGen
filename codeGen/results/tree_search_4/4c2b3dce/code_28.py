import sys

# Initialize a 2D boolean table dp of size (len(s) + 1) x (2)
dp = [[False, False] for _ in range(len(s)+1)]

# Initialize state transitions dictionary
state_transitions = {}

# Iterate over the string s from left to right:
for i in range(1, len(s)+1):
    if s[i-1:i+1] == 'AB':
        dp[i][0] = True
        for j in range(i-1, -1, -1):
            state_transitions[(j, 0)] = (i, 0)
    elif s[i-1:i+1] == 'BA':
        dp[i][1] = True
        for j in range(len(s)-i, i+1):
            state_transitions[(j, 1)] = (i, 1)

# Iterate over the string s from right to left:
for i in range(len(s)-2, -1, -1):
    if s[i:i+2] == 'AB':
        dp[i][0] = False
        for j in range(i+1, len(s)+1):
            state_transitions[(j, 0)] = (i, 0)
    elif s[i:i+2] == 'BA':
        dp[i][1] = False
        for j in range(len(s)-i-1, i+1):
            state_transitions[(j, 1)] = (i, 1)

# Check if there's a valid transition from state dp[len(s)-1][1] to 'YES'
if dp[-1][1]:
    print("YES")
else:
    print("NO")

