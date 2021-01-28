def toArray(string):
    array = string.split(',')
    return array

def toArrayOfNumber(string):
    array = string.split(',')
    for i in range(0, len(array)): 
        array[i] = int(array[i])
    return array
