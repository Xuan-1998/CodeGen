def find_min_string(n, k):
    if n <= k:
        return s[:k]
    else:
        delete_last_char = find_min_string(n - 1, k)
        duplicate = find_min_string(n, k)
        return min([delete_last_char, duplicate], key=len)

n, k = map(int, input().split())
s = input()

print(find_min_string(n, k))
