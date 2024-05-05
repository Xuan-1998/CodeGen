def main():
    t = int(input())
    
    for _ in range(t):
        n, q = map(int, input().split())
        signs = input()
        
        queries = []
        for _ in range(q):
            l, r = map(int, input().split())
            queries.append((l, r))
        
        query_results = process_queries(signs, queries)
        
        print(*query_results, sep='\n')

if __name__ == '__main__':
    main()
