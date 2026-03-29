def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, q = map(int, sys.stdin.readline().split())
        arr = list(map(int, sys.stdin.readline()))
        cs, ss = preprocess(arr)
        for _ in range(q):
            l, r = map(int, sys.stdin.readline().split())
            print(process_query(cs, ss, l, r))

if __name__ == '__main__':
    main()
