import sys

def solve():
    N = int(sys.stdin.readline())
    str1 = sys.stdin.readline().strip()
    str2 = sys.stdin.readline().strip()

    # Preprocess strings using suffix trees
    suffix_tree_str1 = {}
    suffix_tree_str2 = {}

    for i in range(N):
        for j in range(i+1, N+1):
            substr = str1[i:j]
            if substr not in suffix_tree_str1:
                suffix_tree_str1[substr] = 0
            suffix_tree_str1[substr] += 1

            substr = str2[i:j]
            if substr not in suffix_tree_str2:
                suffix_tree_str2[substr] = 0
            suffix_tree_str2[substr] += 1

    # Find common substrings
    common_substrings = set()
    for substr, count in suffix_tree_str1.items():
        if substr in suffix_tree_str2 and count == suffix_tree_str2[substr]:
            common_substrings.add(substr)

    # Find non-overlapping substrings
    already_found = set()
    non_overlapping_count = 0
    for substr in sorted(list(common_substrings), reverse=True):
        if not any(substr in s and len(s) > len(substr) for s in already_found):
            already_found.add(substr)
            non_overlapping_count += 1

    print(non_overlapping_count)

if __name__ == "__main__":
    solve()
