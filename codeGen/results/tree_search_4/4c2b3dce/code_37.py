import sys

def main():
    s = sys.stdin.readline().strip()
    i, j = -1, 0
    for c in s:
        if c == 'A' and i == -1:
            i = len(s) - 2
        elif c == 'B' and j == 0:
            j = len(s) - 1
        elif c == 'A' and i > -1:
            i += 1
        elif c == 'B' and j > 0:
            j -= 1
    if i >= len(s) - 2 and j >= len(s) - 1:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
