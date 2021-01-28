def ejercicio1(a,b):
    i = abs(b)
    resultado = 0
    positivo = abs(b) == b
    c = a*-1 if positivo == False else a
    while i>0:
        resultado = resultado + c
        i = i - 1
    return 'El resultado de {}'.format(a) + ' por ' + str(b) + ' es ' + str(resultado)

