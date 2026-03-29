def main():
    while True:
        n, q = map(int, sys.stdin.readline().split())
        if not (1 <= n <= 3*10**5 and 1 <= q <= 3*10**5):
            break

        array = list(sys.stdin.readline().strip())
        for _ in range(q):
            l, r = map(int, sys.stdin.readline().split())
            result = process_query((l, r), *preprocess_array(array))
            print(result)

if __name__ == '__main__':
    main()
