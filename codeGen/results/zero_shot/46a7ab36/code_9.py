t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    possible_words = pow((2*n-1), (m-1), 1000000007)
    print(possible_words)
