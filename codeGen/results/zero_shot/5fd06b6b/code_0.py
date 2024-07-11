n = int(input().strip())
counts = list(map(int, input().strip().split()))

elements = [10**6] * n

for i in reversed(range(n)):
    elements[i] = min(elements[i], counts[i])
    if i > 0:
        elements[i-1] = min(elements[i-1], elements[i]-1)

print(sum(elements))

