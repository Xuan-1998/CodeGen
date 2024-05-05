import sys

def read_input():
    A = sys.stdin.readline().strip()
    B = sys.stdin.readline().strip()
    return A, B

A, B = read_input()
print(max_similarity_score(A, B))
