import sys

def min_changes(s, k):
    # Count 'R's, 'G's, and 'B's in s and the pattern
    s_counts = {'R': 0, 'G': 0, 'B': 0}
    for c in s:
        if c in s_counts:
            s_counts[c] += 1

    pattern_counts = {'R': k // 3, 'G': (k // 3) * 2 % 3, 'B': (k // 3) * 2}

    # Find the minimum number of changes
    min_changes = float('inf')
    for c in s_counts:
        if c not in pattern_counts:
            continue
        changes = abs(s_counts[c] - pattern_counts[c])
        min_changes = min(min_changes, changes)

    return min_changes

def main():
    T = int(input())
    for _ in range(T):
        n, k = map(int, input().split())
        s = input()
        print(min_changes(s, k))

if __name__ == "__main__":
    main()
