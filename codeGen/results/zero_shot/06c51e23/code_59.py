n = int(input())
t = int(input())
fraction = float(input().strip())

i = 0
while i < n and t > 0:
    if int((fraction * (10 ** i)) + 0.5) != 0:
        grade += round(fraction * (10 ** i))
        t -= 1
    i += 1

print(grade)
