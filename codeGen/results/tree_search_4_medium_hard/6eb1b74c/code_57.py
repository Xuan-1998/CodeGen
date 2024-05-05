from collections import defaultdict

def solve():
    t = input().strip()
    n = int(input())
    strings = [input().strip() for _ in range(n)]

    # Preprocess the strings
    string_indices = defaultdict(list)
    for i, s in enumerate(strings):
        for j in range(len(t) - len(s) + 1):
            if t[j:j+len(s)] == s:
                string_indices[s].append((i, j))

    # Find all occurrences of each string in the text
    occurrences = {}
    for s, indices in string_indices.items():
        occurrences[s] = sorted(indices)

    # Sort and merge the occurrences
    steps = 0
    previous_end = -1
    used_strings = []
    for occurrences_of_s in occurrences.values():
        for _, end in occurrences_of_s:
            if end > previous_end:
                steps += 1
                used_strings.append(occurrences_of_s[0][0])
                previous_end = end

    # Output the result
    print(steps)
    for i, s in enumerate(used_strings):
        print(f"{s} {i+1}")


if __name__ == "__main__":
    solve()
