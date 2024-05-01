import sys

def max_common_non_overlapping_substrings():
    N = int(sys.stdin.readline())
    str1, str2 = [list(input().strip()) for _ in range(2)]

    common_substrings = set()
    count = 0
    i = j = 0

    while i < N and j < N:
        window_size = min(N - i, N - j)
        window_substr = "".join([str1[i + k] for k in range(window_size)])
        if window_substr in common_substrings:
            count += 1
            i += window_size
            j += window_size
        else:
            while len(common_substrings) > 0 and next(iter(common_substrings)) != window_substr[:len(next(iter(common_substrings)))]:
                common_substrings.remove(next(iter(common_substrings)))
            if window_substr not in common_substrings:
                common_substrings.add(window_substr)
            i += 1
            j += 1

    print(count)

max_common_non_overlapping_substrings()
