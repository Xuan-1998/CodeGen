def is_subtable_sorted(subtable):
    for col in range(m):
        sorted_col = [row[col] for row in subtable]
        if sorted_col == sorted(sorted_col):
            return True
    return False

result = "Yes"
for l, r in tasks:
    subtable = [row[l-1:r] for row in table[l-1:r]]
    if not is_subtable_sorted(subtable):
        result = "No"
        break

print(result)
