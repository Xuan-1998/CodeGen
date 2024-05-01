import sys

def preprocess_string(s):
    # Create a suffix tree for the string
    pass  # Implement this part

def find_common_substrings(t1, t2):
    # Find common substrings using the suffix trees
    pass  # Implement this part

def max_common_substrings(str1, str2):
    t1 = preprocess_string(str1)
    t2 = preprocess_string(str2)
    return find_common_substrings(t1, t2)

N = int(sys.stdin.readline())
str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()

print(max_common_substrings(str1, str2))
