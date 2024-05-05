python
text = input()
n = int(input())
strings = []
for _ in range(n):
    strings.append(input().strip())

from collections import defaultdict

string_count = defaultdict(int)
for s in strings:
    for i in range(len(text) - len(s) + 1):
        if text[i:i+len(s)] == s:
            string_count[s] += 1

minimum_steps = sum(string_count.values())
print(minimum_steps)

for i, (s, count) in enumerate(string_count.items()):
    for _ in range(count):
        print(f"{i+1} {text.find(s)}")

