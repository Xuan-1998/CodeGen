import sys

def find_x_and_y(a, b):
    x = 0
    while True:
        y = a - x
        if (x ^ y) == b:
            return f"{x} {y}"
        x += 1
        if x > a:
            return "-1"

if __name__ == "__main__":
    a = int(sys.stdin.readline())
    b = int(sys.stdin.readline())
    print(find_x_and_y(a, b))
