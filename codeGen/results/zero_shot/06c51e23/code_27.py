n = int(input())
t = int(input())
fraction = float(input().strip().split('.')[1])

max_grade = fraction

for i in range(len(str(int(fraction * 10)).split('.')[1])):
    rounded_up = (int(fraction * 10) + 0.5) / 10
    rounded_down = int(fraction * 10) // 10

    max_grade = max(max_grade, min(rounded_up, rounded_down))

    t -= 1

    if t <= 0:
        break

print(int(max_grade * 10))
