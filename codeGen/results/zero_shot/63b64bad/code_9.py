code_block:
n = int(input())
sequence = list(map(int, input().split()))

x = 1
y = 0

while True:
    if x <= 0 or x > n:
        break
    
    x += sequence[x]
    y += sequence[x]
    x -= sequence[x]

print(y)
