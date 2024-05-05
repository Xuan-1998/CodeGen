def round_up(num):
    return int(num + 0.5)

def no_rounding(num):
    return num

def max_grade(n, t):
    max_grade = 0
    for i in range(1, n+1):
        if (i <= t):
            max_grade += int('9' * i + '5')
        else:
            break
    return max_grade

def main():
    n = int(input())
    t = int(input())
    print(max_grade(n, t))

if __name__ == "__main__":
    main()
