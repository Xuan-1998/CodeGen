import sys

def main():
    n, m = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(n)]
    
    # Create a dictionary to store the sorted lists of elements from each column
    state = {i: sorted([row[i] for row in table]) for i in range(m)}
    
    # Check if the last k tasks are sorted by comparing their values
    k = int(input())
    for _ in range(k):
        l, r = map(int, input().split())
        subtable = [table[i][j] for i in range(l-1, r) for j in range(m)]
        
        # Check if the subtable is sorted in non-decreasing order
        if all(subtable[j] <= subtable[j+1] for j in range(len(subtable)-1)):
            print("Yes")
            return
        
    print("No")

if __name__ == "__main__":
    main()
