for l, r in tasks:
    for j in range(m):
        # Check if column j is sorted in non-decreasing order
        sorted_column = all(table[i][j] <= table[i+1][j] for i in range(l-1, r))
        if sorted_column:
            result = True
            break
    if result:
        break

print("Yes" if result else "No")
