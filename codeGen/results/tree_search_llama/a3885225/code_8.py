def solve():
    n = int(input())
    s = input()
    
    ones = s.count('1')
    zeros = n - ones
    
    if abs(ones - zeros) <= n // 2:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()
