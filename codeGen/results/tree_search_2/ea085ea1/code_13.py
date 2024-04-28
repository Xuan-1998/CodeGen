from collections import defaultdict

def solve():
    N = int(input())
    str1 = input()
    str2 = input()

    dp = defaultdict(int)
    LCP = 0

    for i in range(N):
        for j in range(N):
            while str1[i + 1:] != str1[:i] and str2[j:] != str2[:j]:
                if str1[i] == str2[j]:
                    LCP += 1
                else:
                    break

    print(LCP)

solve()
