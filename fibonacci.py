#Bryan Paul Freyre Can
#Código Fibonacci

a = 0
b = 1
sumaFibonacci = a + b
limite = int(input('Introduce el límite para la sucesión\nSi el límite es 1000, la sucesión acabará en el número más cercano a 1000 sin superar esa cantidad: '))

while(sumaFibonacci<limite):
    print(sumaFibonacci)
    a = b
    b = sumaFibonacci
    sumaFibonacci = a + b
exit()
