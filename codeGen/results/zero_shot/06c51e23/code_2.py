n, t = map(int, input().split())
fraction = float(input())

max_grade = int(fraction * (10 ** n))

if t >= (max_grade / 9.99) * n:
    max_grade = int(max_grade + 0.01)

print(max_grade)
