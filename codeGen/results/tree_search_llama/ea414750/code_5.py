def count_bear_substrings():
    s = input().strip()
    bear_index_set = set()

    for i in range(len(s)):
        if s[i:i+4] == 'bear':
            bear_index_set.add(i)

    overlap_count = 0
    for i in bear_index_set:
        for j in bear_index_set:
            if i <= j and (j - i) >= 4:  # Check if the pair overlaps
                overlap_count += 1

    return overlap_count

print(count_bear_substrings())
