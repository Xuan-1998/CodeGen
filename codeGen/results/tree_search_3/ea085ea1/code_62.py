import sys

def find_common_substrings():
    N = int(input())
    str1 = input().strip()
    str2 = input().strip()

    common_substrings = set()
    last_seen_end_index = -1

    for i in range(N):
        for j in range(N):
            if str1[i] == str2[j]:
                substring = str1[i:j+1]
                if i >= last_seen_end_index + 1:
                    common_substrings.add(substring)
                    last_seen_end_index = j
                break

    print(len(common_substrings))

if __name__ == '__main__':
    find_common_substrings()
