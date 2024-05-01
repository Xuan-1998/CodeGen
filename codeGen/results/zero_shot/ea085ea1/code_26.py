import sys

def solve():
    N = int(sys.stdin.readline())
    str1 = sys.stdin.readline().strip()
    str2 = sys.stdin.readline().strip()

    # Generate all possible substrings for both strings
    substrings_str1 = [str1[i:j+1] for i in range(N) for j in range(i, N)]
    substrings_str2 = [str2[i:j+1] for i in range(N) for j in range(i, N)]

    # Compare these substrings and count the number of matches
    common_substrings = 0
    for substring_str1 in substrings_str1:
        if substring_str1 in substrings_str2:
            common_substrings += 1

    print(common_substrings)

if __name__ == "__main__":
    solve()
