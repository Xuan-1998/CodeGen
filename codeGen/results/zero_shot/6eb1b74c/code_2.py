import sys

def generate_substrings(text):
    n = len(text)
    substrings = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            substrings.append(text[i:j])
    return substrings

def count_occurrences(substrings, strings):
    occurrences = [0] * len(strings)
    for substring in substrings:
        for i, s in enumerate(strings):
            if substring == s:
                occurrences[i] += 1
    return occurrences

def min_steps(occurrences):
    total_occurrences = sum(occurrences)
    min_steps = 0
    remaining_occurrences = total_occurrences
    for occurrence in occurrences:
        if remaining_occurrences >= occurrence:
            min_steps += 1
            remaining_occurrences -= occurrence
        else:
            break
    return min_steps + (total_occurrences % len(occurrences) > 0)

def generate_solution(min_steps, occurrences):
    for _ in range(min_steps):
        max_occurrence = 0
        max_index = 0
        for i, occurrence in enumerate(occurrences):
            if occurrence > max_occurrence:
                max_occurrence = occurrence
                max_index = i
        print(f"{max_index} {max_index + occurrences[max_index]}")
        occurrences[max_index] = 0

text = sys.stdin.readline().strip()
n = int(sys.stdin.readline())
strings = []
for _ in range(n):
    strings.append(sys.stdin.readline().strip())

substrings = generate_substrings(text)
occurrences = count_occurrences(substrings, strings)

min_steps = min_steps(occurrences)
print(min_steps)

if min_steps > 0:
    generate_solution(min_steps, occurrences)
else:
    print(-1)
