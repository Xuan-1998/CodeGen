n = int(input())
sequence = list(map(int, input().split()))
sequence.sort()

res = 0
count = 0
for el in sequence:
    if el > count:
        count += 1
    else:
        count = el
    res += count

print(res)

