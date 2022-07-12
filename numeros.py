


#comprobar si un numero es triangular
def es_triangular(n):
    for i in range(1,n+1):
        if i*(i+1)/2 == n:
            return True
    return False


#comprobar si un numero es perfecto
def es_perfecto(n):
    suma = 0
    for i in range(1,n):
        if n%i == 0:
            suma += i
    if suma == n:
        return True
    return False

def es_palindromo(n):
    n = str(n)
    if n == n[::-1]:
        return True
    return False
triangulares = []
perfectos = []
palindromos = []

for i in range(1,10000):
    if es_triangular(i):
        triangulares.append(i)
    if es_perfecto(i):
        perfectos.append(i)
    if es_palindromo(i):
        palindromos.append(i)

print("triangulares")
print()
for i in triangulares:
    print(i)

print("perfectos")
print()
for i in perfectos:
    print(i)

print("palindromos")
print()
for i in palindromos:
    print(i)
