import sys

def preprocess_string(s):
    # Create a suffix tree for the input string
    pass  # implement this function later

def find_common_substrings(str1, str2):
    # Find all common non-overlapping substrings between str1 and str2
    # using the preprocessed suffix trees
    pass  # implement this function later

def main():
    N = int(sys.stdin.readline())
    str1 = sys.stdin.readline().strip()
    str2 = sys.stdin.readline().strip()

    # Preprocess the input strings
    str1_tree = preprocess_string(str1)
    str2_tree = preprocess_string(str2)

    # Find common substrings
    max_common_substrings = find_common_substrings(str1, str2)

    print(max_common_substrings)

if __name__ == '__main__':
    main()
