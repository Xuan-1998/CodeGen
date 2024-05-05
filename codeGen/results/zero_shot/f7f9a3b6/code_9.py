import sys

def solve(s, a):
    n = len(s)
    res = []
    for i in range(n):
        cnt = 0
        for j in range(i+1, n+1):
            flag = True
            for k in range(26):
                if s[i:j].count(chr(k+97)) > a[k]:
                    flag = False
                    break
            if flag:
                cnt += (j - i)
            else:
                break
        res.append(cnt)

    min_res = min(res)
    max_len = max(len(str(x)) for x in res)
    total_ways = sum(1 for x in res if x == min_res) % (10**9 + 7)
    
    print(total_ways, file=sys.stderr)
    print(max_len, file=sys.stderr)
    print(min_res, file=sys.stderr)

if __name__ == "__main__":
    n = int(input())
    s = input()
    a = list(map(int, input().split()))
    solve(s, a)
