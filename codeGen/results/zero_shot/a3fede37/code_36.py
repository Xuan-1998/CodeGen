import sys

def read_input():
    # Read the input from stdin
    n = int(sys.stdin.readline())
    tree = [0] * (2*n)
    
    for i in range(n):
        parent, left, right = map(int, sys.stdin.readline().split())
        tree[2*i] = parent
        tree[2*i+1] = left
        tree[2*i+2] = right
    
    return n, tree

def max_path_sum(tree):
    # Your solution code here
    pass

if __name__ == "__main__":
    n, tree = read_input()
    print(max_path_sum(tree))
