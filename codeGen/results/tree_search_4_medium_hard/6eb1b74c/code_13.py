from collections import defaultdict

def min_steps_to_color_all(text, strings):
    # Create a dictionary to store all occurrences of each string in the text
    occurrences = defaultdict(list)
    for i, s in enumerate(strings):
        idxs = [j.start() for j in (m.start() for m in re.finditer(s, text))]
        occurrences[s].extend(idxs)

    # Sort the strings by their first occurrence index and then by length
    sorted_strings = sorted(occurrences.items(), key=lambda x: (x[1][0], len(x[0])))

    min_steps = 0
    used_strings = set()
    for string, idxs in sorted_strings:
        if not used_strings or max(idxs) > used_strings.pop().start():
            min_steps += 1
            used_strings.update(idxs)

    return min_steps


# Test the function
test_cases = []
while True:
    try:
        t = input().strip()
        n = int(input())
        strings = [input().strip() for _ in range(n)]
        test_cases.append((t, strings))
    except EOFError:
        break

for t, s in test_cases:
    print(min_steps_to_color_all(t, s), end='\n\n')
    for string in s:
        occurrences = [(m.start(), m.end()) for m in (re.finditer(string, t))]
        for idx, _ in sorted(occurrences):
            print(f"{string} {idx}")
