def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(1, n):
        result = simulate_program(a[i-1:i+1])
        if result == float('inf'):
            print(-1)
        else:
            print(result)

if __name__ == '__main__':
    main()
