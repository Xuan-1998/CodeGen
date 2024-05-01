from collections import defaultdict

def find_shortest_uncommon_subsequence():
    S = input().strip()
    T = input().strip()

    if not S or not T:
        return -1

    dp = defaultdict(list)
    for i in range(len(S)):
        prefix = S[:i+1]
        for j in range(min(i+1, len(T))):
            suffix = T[:j+1]
            if prefix == suffix:
                dp[(prefix, i)].append(j)

    shortest_length = float('inf')
    for (prefix, i), indices in dp.items():
        for j in sorted(indices):
            if not T.startswith(prefix + S[i+1:]):
                shortest_length = min(shortest_length, len(S) - i - 1)
                break
        else:
            continue
        break

    return shortest_length if shortest_length != float('inf') else -1


if __name__ == "__main__":
    print(find_shortest_uncommon_subsequence())
