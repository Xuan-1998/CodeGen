code
while True:
    x = int(input())
    b = int(input())
    for y in range(x+1):
        if x + y == a and x ^ y == b:
            print(f"{x} {y}")
            break
    else:
        print("-1")
