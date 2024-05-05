def solve():
    t = input().strip()
    n = int(input())
    strings = [input().strip() for _ in range(n)]

    # Create a Trie to store all the strings
    trie = {}
    for s in strings:
        node = trie
        for c in s:
            if c not in node:
                node[c] = {}
            node = node[c]

    min_steps = 0
    steps = []
    current_position = 0

    while True:
        # Find the longest string that starts at the current position
        found = False
        for i, s in enumerate(strings):
            if s.startswith(t[current_position:current_position + len(s)]):
                node = trie
                for c in s:
                    if c not in node:
                        break
                    node = node[c]
                if 'end' not in node:
                    # This string can be used to color the current position and beyond
                    steps.append((i, current_position))
                    min_steps += 1
                    found = True
                    break
        if found:
            current_position += len(strings[0])
        else:
            # We've reached the end of the text without finding a string to cover it
            print(-1)
            return

    print(min_steps)

    for w, p in steps:
        print(f"{w} {p}")

if __name__ == "__main__":
    solve()
