def main():
    n, x = map(int, input().split())
    
    if n > 19 or x >= 10**n:
        return -1
    
    digits = len(str(x))
    operations = digits - n
    
    return operations

if __name__ == "__main__":
    print(main())
