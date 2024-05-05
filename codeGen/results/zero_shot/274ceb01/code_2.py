n = int(input())
marks_below_water = [0] * (n + 1)

for i in range(1, n + 1):
    m_i = int(input())
    marks_below_water[i] = i - m_i

min_sum_marks_below_water = sum(marks_below_water[1:])

print(min_sum_marks_below_water)
