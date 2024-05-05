def find_smallest_string(s, k):
    if len(s) <= k:
        return s
    if k > len(s):
        if s + s <= s[-1] + s:
            return s[:-1]
        else:
            return s * 2
    return s

# read input from stdin
n, k = map(int, input().split())
s = input()

# print the result to stdout
print(find_smallest_string(s, k))
