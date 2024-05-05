for l, r in tasks:
    subtable = [row[i] for row in table[l-1:r]]  # extract subtable
    for col in range(m):  # iterate through each column
        if not all(subtable[j] <= subtable[j+1] for j in range(len(subtable)-1)):  # check if column is sorted
            print("No")
            break
    else:
        print("Yes")  # found a sorted column, so the answer is "Yes"
