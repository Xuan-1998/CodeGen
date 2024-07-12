python
import sys

def main():
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    array = list(map(int, data[1:n+1]))
    
    # Calculate the sum of absolute values of the array elements
    result = sum(abs(x) for x in array)
    
    print(result)

if __name__ == "__main__":
    main()

