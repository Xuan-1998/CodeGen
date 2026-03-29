import sys

def process_queries(signs, queries):
    for l, r in queries:
        neg_count = 0
        for i in range(l-1, r):
            if signs[i] == '-':
                neg_count += 1
        print(neg_count)

n, q = map(int, input().split())
signs = list(input())
queries = []
for _ in range(q):
    l, r = map(int, input().split())
    queries.append((l, r))
process_queries(signs, queries)
