def is_sorted_subtable(subtable):
    for col in range(m):
        sorted_col = [x for x in subtable[:, col] if x != 0]
        if not all(sorted_col[i] <= sorted_col[i+1] for i in range(len(sorted_col)-1)):
            return False
    return True

for task in tasks:
    l, r = task
    subtable = [row[l-1:r] for row in table]
    if is_sorted_subtable(subtable):
        print("Yes")
    else:
        print("No")
