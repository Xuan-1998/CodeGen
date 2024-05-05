import sys

def solve():
    n = int(input())
    s = input()
    a = list(map(int, input().split()))

    # Calculate the total count of each character in string s
    counts = [0] * 26
    for char in s:
        counts[ord(char) - ord('a')] += 1

    # Initialize variables to store the results
    ways_to_split = 0
    max_len_substring = 0
    min_num_substrings = n

    # Calculate the number of ways to split, max length substring and minimum number of substrings
    for i in range(26):
        count = counts[i]
        if a[i] < count:
            continue

        # Check if it is possible to create at least one substring with a[i] occurrences
        if n % (a[i] + 1) != 0 or n // (a[i] + 1) > 26 - i:
            break

        ways_to_split += 1
        max_len_substring = max(max_len_substring, a[i])
        min_num_substrings = min(min_num_substrings, n // (a[i] + 1))

    # Calculate the minimum number of substrings in case where all characters occur only once
    if ways_to_split == 0:
        ways_to_split = 1
        max_len_substring = len(s)
        min_num_substrings = 1

    print(ways_to_split % (10**9 + 7))
    print(max_len_substring)
    print(min_num_substrings)

if __name__ == "__main__":
    solve()
