import sys

n = int(sys.stdin.readline())
count = 1
i = 1

while True:
    if i ** 0.5 == int(i ** 0.5):
        if (count - 1) * i + i <= n:
            break
    i += 1

print(count)
