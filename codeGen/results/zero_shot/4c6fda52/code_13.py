def min_changes():
    q = int(input())  # number of queries
    for _ in range(q):
        n, k = map(int, input().split())
        s = input()[:k-1]  # first k-1 characters of s
        freq = {'R': 0, 'G': 0, 'B': 0}  # frequency count
        for c in s:
            freq[c] += 1

        changes = sum(freq.values())  # initial changes needed
        remaining = n - k + 1  # length of remaining part of s
        for i in range(remaining):
            if (i % 3) != freq[s[i]]:
                changes += 1

        print(changes)

min_changes()
