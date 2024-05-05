def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        p = [int(x) for x in input().split()]
        l = [int(x) for x in (input() for _ in range(n))][:]
        r = [int(x) for x in (input() for _ in range(n))][:]
        
        # Calculate the minimum number of operations
        min_ops_needed = min_ops(1, l[0], r[0])
        
        print(min_ops_needed)

if __name__ == '__main__':
    main()
