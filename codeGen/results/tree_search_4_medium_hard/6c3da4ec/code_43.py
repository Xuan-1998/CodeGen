def solve():
    n = int(input())
    s = input()
    
    max_or_val = 0
    
    for i in range(n):
        for j in range(i+1, n):
            or_val = 0
            for k in range(i, j+1):
                or_val |= 1 << (s[k] == '1')
            max_or_val = max(max_or_val, or_val)
    
    print(bin(max_or_val)[2:].zfill(n))

if __name__ == "__main__":
    solve()
