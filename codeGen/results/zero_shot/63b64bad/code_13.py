# let's break down the problem step by step
import sys

def process_sequence():
    n = int(input())  # read the length of the sequence
    sequence = list(map(int, input().split()))  # read the sequence itself
    
    for i in range(2, n+1):
        x, y = 1, 0  # initialize x and y
        while True:
            if x <= 0 or x > i:  # check termination condition
                break
            x += sequence[x]
            y += sequence[x]
            x -= sequence[x]
        
        print(y)  # print the final value of y for each run

if __name__ == "__main__":
    process_sequence()
