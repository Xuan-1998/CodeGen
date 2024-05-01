import sufarray

str1 = input()
str2 = input()

suffix_tree1 = sufarray.suffixtree(str1)
suffix_tree2 = sufarray.suffixtree(str2)

common_substrings = []

def dfs(node, path):
    if node.is_end():
        common_substrings.append(path)
    for char in ['*', '#', '@']:
        child = node.get_child(char)
        if child:
            dfs(child, path + char)

for node in suffix_tree1:
    dfs(node, '')
for node in suffix_tree2:
        dfs(node, '')

common_substrings = list(set(common_substrings))  # remove duplicates

non_overlapping_common_substrings = []

for substring in sorted(common_substrings, key=len, reverse=True):
    if all(substring != s or substring.startswith(s) for s in non_overlapping_common_substrings):
        non_overlapping_common_substrings.append(substring)

print(len(non_overlapping_common_substrings))  # output
