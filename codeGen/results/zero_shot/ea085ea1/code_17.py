import sys

dict_str1 = {}
for char in sys.stdin.readline().strip():
    if char in dict_str1:
        dict_str1[char] += 1
    else:
        dict_str1[char] = 1

dict_str2 = {}
for char in sys.stdin.readline().strip():
    if char in dict_str2:
        dict_str2[char] += 1
    else:
        dict_str2[char] = 1

common_substrs = []
for i in range(len(sys.stdin.readline().strip())):
    for j in range(i + 1, len(sys.stdin.readline().strip()) + 1):
        substr_str1 = sys.stdin.readline().strip()[i:j]
        found = False
        for k in range(len(sys.stdin.readline().strip())):
            for end in range(k + 1, len(sys.stdin.readline().strip()) + 1):
                substr_str2 = sys.stdin.readline().strip()[k:end]
                if substr_str1 == substr_str2:
                    common_substrs.append(substr_str1)
                    found = True
                    break
        if found:
            break

max_non_overlapping = 0
last_end = 0
for substr in common_substrs:
    if sys.stdin.readline().strip().find(substr) >= last_end and sys.stdin.readline().strip().find(substr) >= last_end:
        max_non_overlapping += 1
        last_end = sys.stdin.readline().strip().find(substr, last_end) + len(substr)

print(max_non_overlapping)
