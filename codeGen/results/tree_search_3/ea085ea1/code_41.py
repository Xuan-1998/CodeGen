import sys

def build_suffix_array(s):
    n = len(s)
    sa = list(range(n))
    s += '#'
    for i in range(1, n+1):
        j = int(s[i-1])
        sa[j] = i-1
    return sa

def build_suffix_tree(sa):
    tree = {0: []}
    for node_id in sa:
        node = 0 if node_id == 0 else node_id
        while True:
            leaf = tree.get(node, None)
            if leaf is not None:
                break
            node += 1
            tree[node] = [node-1]
    return tree

def find_common_substrings(s1, s2):
    sa1 = build_suffix_array(s1)
    sa2 = build_suffix_array(s2)
    st1 = build_suffix_tree(sa1)
    st2 = build_suffix_tree(sa2)

    max_count = 0
    for node_id in st1:
        if node_id > 0 and st2.get(node_id, None):
            start_idx = st1[node_id][0]
            end_idx = sa1[start_idx] - 1
            common_substr = s1[start_idx:end_idx+1]
            max_count += 1

    return max_count

def main():
    N = int(sys.stdin.readline().strip())
    str1 = sys.stdin.readline().strip()
    str2 = sys.stdin.readline().strip()

    result = find_common_substrings(str1, str2)
    print(result)

if __name__ == "__main__":
    main()
