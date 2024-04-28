str1 = input().strip()
str2 = input().strip()

max_count = 0
for i in range(len(str1)):
    for j in range(i + 4, len(str1) + 1):
        substr = str1[i:j]
        count = 0
        k = 0
        while k < len(str2) and k < len(substr):
            if str2[k] == substr[k]:
                count += 1
                k += 1
            else:
                break
        max_count = max(max_count, count)

print(max_count)
