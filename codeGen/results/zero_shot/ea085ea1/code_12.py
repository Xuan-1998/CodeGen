import sys

def build_suffix_tree(string):
    # Implement a suffix tree construction algorithm, such as Ukkonen's algorithm
    pass

def find_common_substrings(str1, str2):
    # Build suffix trees for both strings
    suffix_tree1 = build_suffix_tree(str1)
    suffix_tree2 = build_suffix_tree(str2)

    # Initialize the maximum number of common non-overlapping substrings
    max_common_substrings = 0

    # Iterate through the suffix trees and find common substrings
    for node in suffix_tree1:
        if node in suffix_tree2:
            # Check if the substring is non-overlapping
            pass

    return max_common_substrings

def main():
    N = int(sys.stdin.readline())
    str1 = sys.stdin.readline().strip()
    str2 = sys.stdin.readline().strip()

    result = find_common_substrings(str1, str2)
    print(result)

if __name__ == "__main__":
    main()
