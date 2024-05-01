def find_max_common_substrings():
    str1 = input()
    str2 = input()

    max_common_substrings = 0

    for i in range(len(str1)):
        for j in range(i + 1, len(str1) + 1):
            substring = str1[i:j]
            if substring in str2:
                max_common_substrings += 1

    print(max_common_substrings)

find_max_common_substrings()
