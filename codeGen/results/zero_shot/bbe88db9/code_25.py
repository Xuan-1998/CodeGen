def main():
    n = int(input())
    p = [int(input()) for _ in range(n)]
    
    print(count_moves(1) % 1000000007)
