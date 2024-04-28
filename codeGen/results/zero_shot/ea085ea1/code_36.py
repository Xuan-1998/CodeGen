str1 = input().strip()
str2 = input().strip()

max_count = 0
for i in range(len(str1)):
    for j in range(i + 1, len(str1) + 1):
        substr = str1[i:j]
        if substr in str2:
            count = 0
            k = i
            while k < len(str1) and str1[k:k+len(substr)] in str2:
                count += 1
                k += len(substr)
            max_count = max(max_count, count)

print(max_count)
