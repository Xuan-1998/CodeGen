for task in tasks:
    l, r = task
    for j in range(m):  # loop through each column
        column = [row[j] for row in table[l-1:r]]  # extract the subtable column
        if is_sorted(column):
            print("Yes")
            exit()  # we found a sorted column, so we can exit

print("No")

def is_sorted(lst):
    return all(x <= y for x, y in zip(lst, lst[1:]))
