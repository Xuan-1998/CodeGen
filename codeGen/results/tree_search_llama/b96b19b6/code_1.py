def remove_duplicates(Str):
    Str = Str.lower()  # Convert the string to lowercase for simplicity
    unique_chars = {}
    result = []
    
    for char in Str:
        if char not in unique_chars:
            unique_chars[char] = True
            result.append(char)
    
    print(''.join(result))

if __name__ == "__main__":
    Str = input()
    remove_duplicates(Str)
