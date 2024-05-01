import sys

# Read input from stdin
N = int(sys.stdin.readline())
str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()

# Initialize count of common substrings
count = 0

# Generate all substrings for str1 and str2
for i in range(N):
    for j in range(i, N):
        substring1 = str1[i:j+1]
        found = False
        for k in range(len(str2)):
            if str2[k:k+len(substring1)] == substring1:
                count += 1
                found = True
                break
        if not found:
            for l in range(k + len(substring1), len(str2)):
                if str2[k:l+1] == substring1:
                    count += 1
                    found = True
                    break

print(count)
