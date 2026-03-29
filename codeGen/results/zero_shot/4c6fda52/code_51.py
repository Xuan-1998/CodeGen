def min_changes_to_appear_in_infinite_string():
    n, k = map(int, input().split())
    s = input()

    min_changes = float('inf')

    for i in range(n - k + 1):
        substring = s[i:i+k]
        infinite_pattern = substring[:k//3] * (3 - (k % 3))  # calculate the infinite pattern
        changes_needed = sum(c1 != c2 for c1, c2 in zip(substring, infinite_pattern))
        min_changes = min(min_changes, changes_needed)

    print(min_changes)
