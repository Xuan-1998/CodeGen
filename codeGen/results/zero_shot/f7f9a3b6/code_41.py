def solve(s, a):
    n = len(s)
    ways = 0
    longest_substring = 0
    min_substrings = float('inf')

    for i in range(n):
        count = 1
        for j in range(i+1, n):
            if ord(s[j]) - ord('a') < a[ord(s[j]) - ord('a')]:
                break
            count += 1

        ways += (count > 0)
        longest_substring = max(longest_substring, count)

        min_substrings = min(min_substrings, n // count + 1)

    return ways % (10**9 + 7), longest_substring, min_substrings


n = int(input())
s = input().strip()
a = [int(x) for x in input().split()]

ways, longest_substring, min_substrings = solve(s, a)
print(ways)
print(longest_substring)
print(min_substrings)
