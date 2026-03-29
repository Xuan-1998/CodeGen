# Let's start by breaking down the problem into smaller sub-problems
# We can consider each element of sequence b as a segment, and check if it can be obtained from some sequence a
# For simplicity, let's assume that we are given sequence a along with sequence b
# The goal is to split a into segments such that their lengths match the elements in sequence b

# First, let's define a function to generate all possible combinations of segment lengths
def generate_segments(a):
    n = len(a)
    segments = []
    for i in range(n - 1):
        segments.append([a[i], a[i + 1]])
    return segments

# Next, we can check if any combination of segment lengths matches the elements in sequence b
def match_segments(segments, b):
    for segment in segments:
        if sorted(segment) == sorted(b):
            return True
    return False

# Now, let's test our solution using the given problem constraints
t = int(input())  # Number of test cases
for _ in range(t):
    n = int(input())  # Size of sequence b
    a = list(map(int, input().split()))  # Sequence a
    b = list(map(int, input().split()))  # Sequence b
    segments = generate_segments(a)
    if match_segments(segments, b):
        print("YES")
    else:
        print("NO")
