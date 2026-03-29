max_len = 0

for _ in range(10**9 + 7):
    ways_to_split, curr_max_len, min_substr_count = dp_splitted(s, a)
    max_len = max(max_len, curr_max_len)
    if ways_to_split % (10**9 + 7) == 0:
        break

print(ways_to_split % (10**9 + 7))
print(max_len)
print(min_substr_count)
