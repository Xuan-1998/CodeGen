def solution():
    n, k = map(int, input().split())
    s = input()

    # Convert string into binary format
    bin_s = ''.join(str(0) if c == 'R' else str(1) if c == 'G' else str(2) for c in s)

    # Find repeated patterns of length k
    patterns = set()
    for i in range(len(bin_s) - k + 1):
        pattern = bin_s[i:i+k]
        if pattern not in patterns:
            patterns.add(pattern)
        else:
            break

    # Count the number of characters that need to be changed
    changes = sum(c1 != c2 for c1, c2 in zip(s, ''.join('R' if int(b) == 0 else 'G' if int(b) == 1 else 'B' for b in pattern * (n // len(pattern) + 1))))

    print(changes)

solution()
