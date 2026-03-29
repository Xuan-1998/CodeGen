def solve():
    n, k = map(int, input().split())
    s = input()
    
    if k >= n:
        code = ""
        while len(code) < k:
            code += s
        print(code[:k])
    else:
        if s[k-1] < s[0]:
            print(s[:k])
        else:
            print(s + s[:k-1])

solve()
