from sys import stdin

def solve():
    s = stdin.readline().strip()
    seen_a = False
    for char in s:
        if char == 'A':
            seen_a = True
        elif char == 'B' and seen_a:
            print("YES")
            return
    print("NO")

if __name__ == "__main__":
    solve()
