def main():
    commands = input()  # receive input string of commands
    n = int(input())  # receive input integer for number of modifications

    modified_commands = modify_commands(commands, n)
    max_distance = calculate_max_distance(modified_commands)

    print(max_distance)  # print the maximum distance to stdout

if __name__ == "__main__":
    main()
