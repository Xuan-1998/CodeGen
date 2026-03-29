import sys

def process_input():
    T = int(input())
    for _ in range(T):
        N, M, C = map(int, input().split())
        upper_radii = list(map(int, input().split()))
        lower_radii = list(map(int, input().split()))
        
        # Your code here...
