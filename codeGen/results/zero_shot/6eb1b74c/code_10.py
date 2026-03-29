import sys

def solve():
    t = input().strip()
    n = int(input())
    s = [input().strip() for _ in range(n)]

    # Count occurrences of each string in the text
    counts = {s[i]: 0 for i in range(n)}
    for i in range(len(t)):
        for j in range(i+1, len(t)+1):
            substring = t[i:j]
            if substring in s:
                counts[substring] += 1

    # Sort strings by count
    sorted_s = [x for _, x in sorted(counts.items(), key=lambda item: item[1], reverse=True)]

    min_steps = 0
    covered_chars = set()
    used_strings = []
    for string in sorted_s:
        occurrences = t.count(string)
        if occurrences > 0 and not (set(string).issubset(covered_chars)):
            min_steps += 1
            covered_chars.update(set(string))
            used_strings.append((len(used_strings)+1, len(t)))
        else:
            break

    # Print solution
    print(min_steps)
    for pair in used_strings:
        print(*pair)

if __name__ == "__main__":
    solve()
