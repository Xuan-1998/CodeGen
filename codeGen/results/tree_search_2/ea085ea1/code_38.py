import sys

def read_input():
    n = int(sys.stdin.readline().strip())
    str1 = sys.stdin.readline().strip()
    str2 = sys.stdin.readline().strip()
    return n, str1, str2

def preprocess_string(str):
    # Pre-process the string to create a suffix tree.
    pass

n, str1, str2 = read_input()

# Pre-process both strings
preprocess_string(str1)
preprocess_string(str2)

dp_table = [[False] * (len(str2) + 1) for _ in range(len(str1) + 1)]
max_common_substrings = 0

for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        if str1[i - 1] == str2[j - 1]:
            dp_table[i][j] = dp_table[i - 1][j - 1]
        else:
            dp_table[i][j] = False

for k in range(len(str2)):
    for l in range(k + 1, len(str2) + 1):
        if dp_table[0][l - k]:
            max_common_substrings += 1
            j = l - k
            while j > 0 and not dp_table[0][j - 1]:
                j -= 1
            i = 0
            while str1[i] == str2[k]:
                i += 1
                if i >= len(str1):
                    break

print(max_common_substrings)
