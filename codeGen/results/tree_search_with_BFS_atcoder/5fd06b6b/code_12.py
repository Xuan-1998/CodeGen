n = int(input().strip())
sequence = list(map(int, input().strip().split()))
sequence.sort()

sum = 0
prev = -1
for x in sequence:
    if x > prev:
        sum += x
        prev = x
    else:
        sum += prev
        prev -= 1
print(sum)

