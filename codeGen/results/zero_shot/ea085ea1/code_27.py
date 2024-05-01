import sys
from collections import defaultdict

def preprocess_string(s):
    # Create a suffix tree for the string
    suffixes = [s[i:] for i in range(len(s))]
    suffix_tree = defaultdict(list)
    for suf in suffixes:
        for i in range(len(suf)):
            suffix_tree[suf[i:]][i].append(suf)
    return suffix_tree

def find_common_substrings(str1, str2):
    # Create preprocess strings
    str1_suffix_tree = preprocess_string(str1)
    str2_suffix_tree = preprocess_string(str2)

    max_common_substrings = 0
    for k in str1_suffix_tree:
        for j in str2_suffix_tree:
            if k == j:  # Common substring found
                for i in range(min(len(k), len(j))):
                    common_substr = k[i:]
                    if str1.find(common_substr) != -1 and str2.find(common_substr) != -1:
                        max_common_substrings += 1
    return max_common_substrings

def main():
    N = int(sys.stdin.readline())
    str1 = sys.stdin.readline().strip()
    str2 = sys.stdin.readline().strip()

    result = find_common_substrings(str1, str2)
    print(result)

if __name__ == "__main__":
    main()
