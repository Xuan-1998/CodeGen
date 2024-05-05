import sys

def parse_input():
    t = input().strip()
    n = int(input())
    s_strings = []
    for i in range(n):
        s_string = input().strip()
        s_strings.append((i, s_string))
    return t, n, s_strings

def min_steps(t, s_strings):
    max_positions = 0
    for _, s_string in s_strings:
        positions = [i for i in range(len(t)) if t[i:i+len(s_string)].lower() == s_string.lower()]
        max_positions = max(max_positions, len(positions))
    return max_positions

def print_output(t, n, s_strings):
    m = min_steps(t, s_strings)
    if m == -1:
        print(-1)
    else:
        print(m)
        for j in range(m):
            positions = [i for i in range(len(t)) if t[i:i+len(s_strings[j][1])].lower() == s_strings[j][1].lower()]
            print(f"{j+1} {positions[0]}")

def main():
    t, n, s_strings = parse_input()
    m = min_steps(t, s_strings)
    if m == -1:
        print(-1)
    else:
        print(m)
        for j in range(m):
            positions = [i for i in range(len(t)) if t[i:i+len(s_strings[j][1])].lower() == s_strings[j][1].lower()]
            print(f"{j+1} {positions[0]}")

if __name__ == "__main__":
    main()
