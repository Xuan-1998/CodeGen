def find_common_substrings():
    N = int(input())
    str1 = input().strip()
    str2 = input().strip()

    # Create a suffix tree for str1
    tree = {}
    for i in range(N, -1, -1):
        node = tree
        for j in range(i, N):
            c = str1[j]
            if c not in node:
                node[c] = {}
            node = node[c]

    # Create a Z-array for str2
    z_array = [0] * N
    z_index = 0
    for i in range(1, N):
        while (i + z_index > N) or (str2[i - 1] == str2[z_index]):
            z_index += 1
        if z_index == 0:
            z_array[i] = 0
        else:
            z_array[i] = z_index

    # Find the maximum number of common non-overlapping substrings
    max_common_substrings = 0
    for i in range(N):
        for j in range(i, N):
            if str1[i:j+1] in tree and z_array[j-i+1] > 0:
                max_common_substrings += 1

    print(max_common_substrings)

find_common_substrings()
