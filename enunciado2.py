def calcularFactorial(n):
    #calcula factorial de forma no recursiva
    factorial = 1
    for i in range(1,n+1):
        factorial *= i
    return factorial

print(calcularFactorial(5))
print(calcularFactorial(4))
