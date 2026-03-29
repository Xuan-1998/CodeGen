# Take the input
n, m, h, *s = map(int, input().split())
s = s[:m]

# Check if there are enough players to form a team
if n > sum(s):
    print(-1)
else:
    # Calculate the probability
    p = 1 - (sum(s) - s[h-1]) / n ** m
    
    # Print the answer
    print(p)
