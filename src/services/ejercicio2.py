def mayorNumero(array):
    array.sort()
    elem = array.pop()
    return 'El numero mas grande de la lista es: '+str(elem)
