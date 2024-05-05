def can_find(k):
    for i in range(len(s) - k + 1):
        substr = s[i:i+k]
        if set(substr) == {'R', 'G', 'B'}:
            return True
    return False

def min_changes(k):
    min_changes = 0
    for i in range(len(s) - k + 1):
        substr = s[i:i+k]
        infinite_substr = (k//3)*'RGB'[0] + (k%3)*'RGB'[k%3]
        diff_count = sum(c1 != c2 for c1, c2 in zip(substr, infinite_substr))
        min_changes = max(min_changes, k - len(set(substr)))
    return min_changes

while True:
    n, k = map(int, input().split())
    if not n and not k:
        break
    s = input()
    min_changes_k = min_changes(k)
    print(min_changes_k)
