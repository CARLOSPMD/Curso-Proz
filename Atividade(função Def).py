'''Faça uma função calculadora de dois números com três parâmetros: os dois primeiros
serão os números da operação e o terceiro será a entrada que definirá a operação a ser
executada. Considera a seguinte definição:
1. Soma
2. Subtração
3. Multiplicação
4. Divisão

Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.'''

def calcular_numeros(num1,ope,num2):

 if (ope == "+"):
    resultado = int(num1) + int(num2)
 elif (ope == "-"):
    resultado = int(num1) - int(num2)
 elif (ope == "*"):
    resultado = int(num1) * int(num2)
 elif (ope == "/"):
    resultado = int(num1) / int(num2)
 else:
    resultado = 0
 
 
 return resultado

 

num1 = int(input("Digite um numero: "))
ope = input("Digite um operador: ")
num2 = int(input("Digite outro numero: "))

calculadora = calcular_numeros(num1,ope,num2)

print(calculadora)