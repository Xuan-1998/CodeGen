# Read input arrays
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

# Sort both arrays
A.sort()
B.sort()

# Validation function: find a pair (a, b) that meets the requirements
def validate(A, B):
    for a in A:
        for b in B:
            if a + b not in A and a + b not in B:
                return (a, b)
    return None

result = validate(A, B)

if result is not None:
    print(*result)  # Print the pair
else:
    print("No such pair found")  # Output when no valid pair exists
