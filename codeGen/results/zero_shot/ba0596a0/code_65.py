from sys import stdin

# Read the input from standard input
stones = list(map(int, stdin.readline().split()))

k = 1
while True:
    if stones[0] + k - 1 == stones[1]:
        break
    elif stones[0] + k not in stones:
        print("NO")
        exit()
    k += 2

print("YES")
