import sys

# Function to preprocess the string and calculate the minimum operations for each prefix
def preprocess(s, n):
    operations = [0] * (n + 1)
    for i in range(1, n):
        operations[i + 1] = operations[i]
        # Check for palindrome of length 2
        if s[i] == s[i - 1]:
            operations[i + 1] += 1
        # Check for palindrome of length 3
        elif i > 1 and s[i] == s[i - 2]:
            operations[i + 1] += 1
    return operations

def main():
    # Read input
    n, m = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().strip()
    
    # Preprocess the string
    operations = preprocess(s, n)
    
    # Process each query
    for _ in range(m):
        l, r = map(int, sys.stdin.readline().split())
        # Calculate the cost for the substring from l to r
        cost = operations[r] - operations[l - 1]
        print(cost)

if __name__ == "__main__":
    main()
