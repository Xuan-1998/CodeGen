import sys

def find_common_substrings():
    # Read input from stdin
    str1 = sys.stdin.readline().strip()
    str2 = sys.stdin.readline().strip()

    max_common = 0

    # Generate all substrings for each string
    for i in range(len(str1)):
        for j in range(i + 1, len(str1) + 1):
            sub_str1 = str1[i:j]

            for k in range(len(str2)):
                for end in range(k + 1, len(str2) + 1):
                    sub_str2 = str2[k:end]

                    # Check if two substrings are equal
                    if sub_str1 == sub_str2:
                        max_common += 1

    print(max_common)

find_common_substrings()
