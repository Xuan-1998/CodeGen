from itertools import zip_longest
n = int(input())
str1 = input()
str2 = input()

max_count = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            substr1 = str1[i:k]
            substr2 = str2[i:j]
            if substr1 == substr2:
                count = 0
                for a, b in zip_longest(str1[k:], str2[j:], fillvalue=''):
                    if a == b:
                        count += 1
                    else:
                        break
                max_count = max(max_count, count)

print(max_count)
