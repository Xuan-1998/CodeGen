text = input()
n = int(input())
strings = []
for i in range(n):
    strings.append(input())

string_occurrences = {}
for i, s in enumerate(strings):
    for j in range(len(text) - len(s) + 1):
        if text[j:j+len(s)] == s:
            if s not in string_occurrences:
                string_occurrences[s] = [j]
            else:
                string_occurrences[s].append(j)

steps = 0
used_strings = set()
for s in strings:
    if s not in used_strings:
        for j in string_occurrences[s]:
            if all(not text[j+x:j+len(s)+x].endswith(s) for x in range(len(s))):
                steps += 1
                break
        used_strings.add(s)

print(steps)
for i in range(steps):
    for s in strings:
        if s not in used_strings:
            for j in string_occurrences[s]:
                if all(not text[j+x:j+len(s)+x].endswith(s) for x in range(len(s))):
                    print(f"{i+1} {j}")
                    break
            used_strings.add(s)
            break
    if i == steps - 1:
        break
