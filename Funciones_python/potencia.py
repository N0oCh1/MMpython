def main():
    print(potencia(9,6))


def potencia(n, base =2):
    result = n 
    for a in range(1, base):
        result *= n   
    return result



if __name__ == "__main__":
    main()