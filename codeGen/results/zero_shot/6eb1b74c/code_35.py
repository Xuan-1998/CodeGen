import sys

def min_steps_to_color_all_letters(t, n, strings):
    total_steps = 0
    steps_left = len(t)
    strings_used = []

    for string in strings:
        occurrences = t.count(string)
        total_steps += occurrences
        steps_left -= len(string) * occurrences

    if steps_left <= 0:
        return -1

    m = total_steps
    print(m)

    j = 1
    for _ in range(m):
        max_len = 0
        max_occurrence = 0
        for i, string in enumerate(strings):
            occurrence = t.count(string)
            if occurrence > 0 and len(string) + occurrence * len(string) <= steps_left:
                max_len = len(string)
                max_occurrence = occurrence
                strings_used.append(i)
                break

        print(j, strings_used[-1])
        steps_left -= max_len * max_occurrence
        j += 1

# Read input from standard input
t = sys.stdin.readline().strip()
n = int(sys.stdin.readline())
strings = [sys.stdin.readline().strip() for _ in range(n)]

min_steps_to_color_all_letters(t, n, strings)
