def main():
    print("serie fibonacci")
    limit = int(input("limite del fibonacci:  "))
    for n in range(limit):
        print (fibonacci(n))


def fibonacci(n):
    if n == 0: 
        return 0
    elif n == 1 or n == 2: 
        return 1
    else: 
        return fibonacci(n-1) + fibonacci(n-2)


if __name__ == "__main__":
    main()