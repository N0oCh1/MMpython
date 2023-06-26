print("Bienvenido, introduzca tres numeros\n")
a = int(input("\nintroduzca el primer numero: "))
b = int(input("\nintroduzca el segundo numero: "))
c = int(input("\nintroduzca el tercer numero: "))

mayor = max(a,b,c)
menor = min(a,b,c)

print("su numero mayor es: {}".format(mayor))
print("su numero menor es: {}".format(menor))
