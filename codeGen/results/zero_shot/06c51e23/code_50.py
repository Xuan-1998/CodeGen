import sys
n, t = map(int, input().split())
frac = float(input())

def round_frac(frac, t):
    max_grade = 0
    for i in range(len(str(frac).split('.')[1])):
        new_frac = "{:.{}f}".format(frac, i+1)
        new_grade = int(new_frac.split('.')[0])
        if new_grade <= 100 and t >= round_time(new_frac):
            max_grade = new_grade
    return max_grade

def round_time(frac):
    time_taken = len(str(frac).split('.')[1]) * 10
    return time_taken + (len(str(frac).split('.')[1]) > 0)

print(round_frac(frac, t))
