t = input().strip()
n = int(input())
strings = [input().strip() for _ in range(n)]
string_indices = {}
for i, s in enumerate(strings):
    string_indices[s] = i

m = 0
for s in strings:
    m = max(m, len(t) - sum(1 for c in t if c in s))

while m > 0:
    used_strings = []
    for j in range(m):
        max_len = 0
        best_s = None
        for s in strings:
            if s not in used_strings and len(t) - sum(1 for c in t if c in s) >= j:
                length = sum(1 for c in t if c in s)
                if length > max_len:
                    max_len = length
                    best_s = s
        used_strings.append(best_s)
    m -= 1

print(m)
for j, s in enumerate(used_strings):
    print(j + 1, string_indices[s] + 1)
