def main(): 
    n1=0
    n2=1 
    cont = 1 
    nex_number = 0
    length = int(input("lenght of Fibonacci: "))
    if length < 0:
        print("please put a positive number")
    else: 
        while cont <= length: 
            print ("{} ".format(nex_number), end="")
            cont +=1
            n1 = n2
            n2 = nex_number
            nex_number = n1 + n2

if __name__ == "__main__":
    main()