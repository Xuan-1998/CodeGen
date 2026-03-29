def main():
    root_node = find_root_node()
    min_inversed_roads = min_inversed_roads()
    possible_capitals = find_possible_capitals()
    
    print(min_inversed_roads)
    for capitals in possible_capitals:
        print(' '.join(map(str, capitals)))

if __name__ == '__main__':
    main()
