code = """

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    len_res = (m // 9) * len(str(n)) + min(len(str(n)), m % 9)
    print(len_res % (10**9+7))

"""

