code = ""
while True:
    c = sys.stdin.read(1)
    if c == "\n":
        break
    code += c
n, t = map(int, code.split()[:2])
f = float(code.split()[2])

max_grade = 0
seconds_taken = 0
for i in range(1, n + 1):
    rounded_f = round(f, i)
    seconds_taken += len(str(rounded_f)) * i
    max_grade = max(max_grade, int(10 ** i) + (rounded_f - 0.5) // (1 / 10 ** i))
    if seconds_taken > t:
        break

print(max_grade)
