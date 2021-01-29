### Escribir una función que cuente la cantidad de veces que se repite una palabra

def contar_repeticiones(string):
    lowercase = string.lower()
    array = lowercase.split(' ')
    counted = []
    message = ''

    for element in array:
        if element not in counted:
            count = array.count(element)
            counted.append(element)
            message += '\n'+element + ': ' + str(count)
    
    return message



