import sys

n = int(sys.stdin.readline())
t = int(sys.stdin.readline())
fraction = sys.stdin.readline().strip()

fraction_float = float(fraction)

max_grade = 0
for i in range(n):
    max_digit_grade = int((10 ** (n - i - 1)) * fraction_float) // (10 ** (n - i))
    max_grade += max_digit_grade

sys.stdout.write(str(max_grade) + '\n')
