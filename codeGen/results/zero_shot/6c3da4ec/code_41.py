import sys

def solve():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()

    max_or_value = 0
    for i in range(n):
        for j in range(i + 1, n):
            substring1 = s[i:j+1]
            for k in range(j + 1, n):
                substring2 = s[j:k+1]
                or_value = int(substring1, 2) | int(substring2, 2)
                max_or_value = max(max_or_value, or_value)

    print(bin(max_or_value)[2:].zfill(n))

if __name__ == "__main__":
    solve()
