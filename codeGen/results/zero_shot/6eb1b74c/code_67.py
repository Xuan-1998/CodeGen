import sys

def solve():
    t = input()
    n = int(input())
    strings = [input() for _ in range(n)]

    m = 0
    pos = 0
    for string in sorted(strings, key=len, reverse=True):
        while pos + len(string) <= len(t):
            if t[pos:pos+len(string)] == string:
                pos += len(string)
                m += 1
                print(f"{m} {pos - len(string) + 1}")
            else:
                break

    if pos < len(t):
        print(-1)

if __name__ == "__main__":
    solve()
