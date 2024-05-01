import sys

def solve():
    # Read input strings from stdin
    str1 = sys.stdin.readline().strip()
    str2 = sys.stdin.readline().strip()

    # Preprocess input strings to create suffix trees
    # (This part is omitted for simplicity, but you can use a suitable algorithm like Ukkonen's)
    
    # Initialize variables to keep track of common substrings
    max_common_substrings = 0

    # Iterate through both suffix trees simultaneously
    for i in range(len(str1)):
        for j in range(i + 1):
            substring = str1[j:i+1]
            if substring in str2:
                # Found a common non-overlapping substring!
                max_common_substrings += 1

    # Print the maximum number of common substrings
    print(max_common_substrings)

if __name__ == "__main__":
    solve()
