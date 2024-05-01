import pytse

# Read input strings from stdin
str1 = input().strip()
str2 = input().strip()

# Create suffix trees for each string
str1_tree = pytse.suffix_tree(str1)
str2_tree = pytse.suffix_tree(str2)

def find_common_substrings(str1_tree, str2_tree):
    common_substrings = []

    # Iterate through nodes in both trees
    for node1 in str1_tree.traverse():
        for node2 in str2_tree.traverse():
            # Check if nodes have a common ancestor
            if node1.common_ancestor(node2):
                # If yes, extract the common substring and add it to the list
                substring = node1.suffix + node2.suffix
                common_substrings.append(substring)

    return common_substrings

common_substrings = find_common_substrings(str1_tree, str2_tree)
max_non_overlapping_substrings = len(set(common_substrings))

print(max_non_overlapping_substrings)  # Print answer to stdout
