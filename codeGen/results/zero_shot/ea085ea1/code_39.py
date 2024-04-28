n = int(input())
str1 = input()
str2 = input()

max_length = 0
max_count = 0
for length in range(1, n):
    for i in range(n - length):
        substring = str1[i:i+length]
        count = (str2.index(substring) if substring in str2 else -1)
        if count != -1:
            max_length = max(max_length, length)
            max_count += 1

print(max_count)
