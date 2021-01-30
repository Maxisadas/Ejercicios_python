## Verificar si una cadena de texto es un palíndromo

def isPalindrome(string):
    lowercase = string.lower()
    stringRight = lowercase.replace(' ','')
    stringReversed = stringRight [::-1]
    if stringRight == stringReversed:
        return 'La palabra '+string+' es un palíndromo'
    else:
        return 'La palabra '+string+' NO es un palíndromo'
