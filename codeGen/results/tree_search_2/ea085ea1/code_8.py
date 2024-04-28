from collections import defaultdict

def solve():
    str1 = input().strip()
    str2 = input().strip()

    # Build Tries for both strings
    trie1 = defaultdict(str)
    for i in range(len(str1)):
        prefix = ""
        for j in range(i, len(str1)):
            prefix += str1[j]
            trie1[prefix] = ""

    trie2 = defaultdict(str)
    for i in range(len(str2)):
        prefix = ""
        for j in range(i, len(str2)):
            prefix += str2[j]
            trie2[prefix] = ""

    # Find common substrings
    count = 0
    for node1 in trie1:
        for node2 in trie2:
            if node1 == node2:
                count += 1

    print(count)

if __name__ == "__main__":
    solve()
