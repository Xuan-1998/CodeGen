import sys

def suffix_tree(str):
    # Create a suffix tree for the input string
    nodes = [None] * (len(str) + 1)
    edges = []
    for i in range(len(str)):
        suffix = str[i:]
        node = None
        for j in range(i, -1, -1):
            if str[j:] == suffix:
                node = j
                break
        edges.append((i, node))
    return nodes, edges

def common_substrings(str1, str2):
    # Find all common substrings between str1 and str2
    nodes1, edges1 = suffix_tree(str1)
    nodes2, edges2 = suffix_tree(str2)
    common_edges = []
    for edge in edges1:
        for other_edge in edges2:
            if edge[0] == other_edge[1]:
                common_edges.append(edge)
                break
    return [edge[1] for edge in common_edges]

def count_substring_occurrences(str, substrings):
    # Count the occurrences of each substring in str
    occurrences = {}
    for substring in substrings:
        occurrences[substring] = 0
        for i in range(len(str)):
            if str[i:i+len(substring)] == substring:
                occurrences[substring] += 1
    return occurrences

def max_non_overlapping_substrings(str1, str2):
    # Find the maximum number of common non-overlapping substrings
    substrings = common_substrings(str1, str2)
    occurrences1 = count_substring_occurrences(str1, substrings)
    occurrences2 = count_substring_occurrences(str2, substrings)
    max_count = 0
    for substring in substrings:
        if occurrences1[substring] and occurrences2[substring]:
            max_count = max(max_count, min(occurrences1[substring], occurrences2[substring]))
    return max_count

def main():
    str1 = sys.stdin.readline().strip()
    str2 = sys.stdin.readline().strip()
    print(max_non_overlapping_substrings(str1, str2))

if __name__ == "__main__":
    main()
