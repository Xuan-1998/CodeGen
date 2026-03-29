def simulate_program(a):
    memo = {}
    for i in range(1, len(a)):
        x, y = 1, 0
        while x > 0 and x <= len(a):
            if (x, y) not in memo:
                x += a[x]
                y += a[x]
                x -= a[x]
                y += a[x]
            else:
                return y
    return -1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    
    for i in range(2, n+1):
        result = simulate_program(a[:i])
        print(result)

if __name__ == "__main__":
    main()
