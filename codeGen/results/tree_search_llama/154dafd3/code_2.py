def main():
    input_str = input()
    numbers = [float(x) for x in input_str.split(',')]
    rounded_numbers = round_to_nearest_multiple_of_5(numbers)
    print(','.join(map(str, rounded_numbers)))

if __name__ == '__main__':
    main()
