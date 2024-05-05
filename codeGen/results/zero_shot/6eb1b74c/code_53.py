text = input()
n = int(input())
strings = [input() for _ in range(n)]

string_hashes = {}
for i, s in enumerate(strings):
    for j in range(len(s)):
        for k in range(j + 1, len(s) + 1):
            substring = s[j:k]
            string_hashes[substring] = (i, j)

occurrences = {}
for substring, (i, j) in string_hashes.items():
    for k in range(len(text)):
        if text[k:k + len(substring)] == substring:
            occurrences.setdefault((i, j), []).append(k)

import heapq

min_steps = 0
covered_occurrences = set()
heap = []
for occurrence_set in occurrences.values():
    for k in occurrence_set:
        if k not in covered_occurrences:
            heapq.heappush(heap, (k, len(occurrence_set)))

solution = []
while heap:
    k, _ = heapq.heappop(heap)
    for i, j in string_hashes.values():
        if k >= j and k < j + len(strings[i]):
            solution.append((i, k - j))

print(min_steps)
for w, p in solution:
    print(w, p)
