if __name__ == "__main__":
    commands = input().strip()
    n = int(input())
    
    # Call the max_distance function
    max_dist = max_distance(commands, n)
    
    print(max_dist)
