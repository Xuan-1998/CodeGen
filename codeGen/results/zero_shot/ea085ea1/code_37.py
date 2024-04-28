n = int(input())
str1 = input().strip()
str2 = input().strip()

def common_substrings(str1, str2):
    max_count = 0
    for i in range(len(str1)):
        for j in range(i + len(str1) - n + 1):
            substr1 = str1[j:j+n]
            count = 0
            for k in range(len(str2)):
                if str2[k:k+n] == substr1:
                    count += 1
            max_count = max(max_count, count)
    return max_count

print(common_substrings(str1, str2))
