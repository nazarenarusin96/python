#El * sirve para saber el tipo de dato y lo convierte en una tupla

def argumento(*num):
    for i in num:
        print(i);

print(argumento(1,2,3,4,5));