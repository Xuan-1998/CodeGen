def find_max_common_substrings():
    # Read input strings from standard input
    N = int(input())
    str1 = input().strip()
    str2 = input().strip()

    # Initialize memoization dictionary
    memo = {}

    max_common = 0

    for i in range(N):
        for j in range(N):
            # Check if the current substrings match
            if str1[i:j+1] == str2[i:j+1]:
                # If they do, increment the count and update memo
                common = 1 + (memo.get((i-1, j-1), 0) if i > 0 and j > 0 else 0)
                memo[(i, j)] = common
                max_common = max(max_common, common)

    print(max_common)

find_max_common_substrings()
