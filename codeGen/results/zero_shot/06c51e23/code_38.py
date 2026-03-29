import sys

def find_max_grade(n, t, dec):
    max_grade = 0
    for i in range(1, n+1):
        if int(dec[i-1:i]) >= 5:
            max_grade += 1
        else:
            while int(dec[i:i+3]) < 500 and i + 3 <= n:
                max_grade -= 4
                i += 3
    return min(max_grade, t)

n, t = map(int, input().split())
dec = input()

print(find_max_grade(n, t, dec))
