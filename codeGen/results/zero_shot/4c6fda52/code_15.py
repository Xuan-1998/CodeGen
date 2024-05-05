def count_changes(s, k):
    changed_count = 0
    i = 0
    while True:
        if len(s[i:i+k]) == k:
            break
        if s[i] != 'R' and s[i] != 'G':
            changed_count += 1
        i += 1
    return changed_count

n = int(input())
k = int(input())
s = input()
print(count_changes(s, k))
