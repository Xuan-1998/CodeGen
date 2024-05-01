def max_common_substrings(str1, str2):
    str1_suffix_tree, str2_suffix_tree = preprocess_strings(str1, str2)
    common_substrings = find_common_substrings(str1_suffix_tree, str2_suffix_tree)
    return count_non_overlapping_substrings(common_substrings)

if __name__ == "__main__":
    str1 = input().strip()
    str2 = input().strip()

    print(max_common_substrings(str1, str2))
