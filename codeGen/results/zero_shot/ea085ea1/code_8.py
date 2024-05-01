import sys
from collections import defaultdict

def find_max_common_substrings():
    N = int(sys.stdin.readline())
    str1 = sys.stdin.readline().strip()
    str2 = sys.stdin.readline().strip()

    # Create a suffix tree or suffix array for str1 and str2
    str1_suffix_tree = {}
    str2_suffix_tree = {}

    # Find the common non-overlapping substrings
    max_count = 0

    return max_count

print(find_max_common_substrings())
