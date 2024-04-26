def solve():
    n = int(input())
    s = input().strip()

    ones = s.count('1')
    zeros = len(s) - ones

    if (ones + zeros) % 2 != 0:
        print("YES")
    else:
        if n <= 2:
            print("NO" if s == s[::-1] else "YES")
        else:
            print("YES")

if __name__ == "__main__":
    solve()
