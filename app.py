from flask import Flask, render_template, request
import src.services.index as index
import src.utility.to_array as array
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/ejercicio1',methods=['POST'])
def ejercicio1():
    try:
        variable1 = int(request.form['variable1'])
        variable2 = int(request.form['variable2'])
    except ValueError:
        return 'Solo se permite valores enteros'
    return index.ejercicio1(variable1,variable2)
@app.route('/ejercicio2',methods=['POST'])
def ejercicio2():
    string = str(request.form['variable1'])
    found = re.search('[^0-9,]+', string)
    if found:
        return 'No se permite letras ni caracteres especiales'
    variable1 = array.toArrayOfNumber(string)
    return index.mayorNumero(variable1)
@app.route('/ejercicio3',methods=['POST'])
def ejercicio3():
    string = str(request.form['variable1'])
    found = re.search('[^A-Za-z0-9 ]+', string)
    if found:
        return 'No se permite caracteres especiales'
    return index.contar_repeticiones(string)
@app.route('/ejercicio4',methods=['POST'])
def ejercicio4():
    string = str(request.form['variable1'])
    found = re.search('[^A-Za-z0-9 ]+', string)
    if found:
        return 'No se permite caracteres especiales'
    return index.isPalindrome(string)
@app.route('/ejercicio5',methods=['POST'])
def ejercicio5():
    string1 = str(request.form['variable1'])
    string2 = str(request.form['variable2'])
    found1 = re.search('[^0-9,-]+', string1)
    found2 = re.search('[^0-9,-]+', string2)
    if found1 or found2:
        return 'No se permite caracteres especiales'
    return index.median(string1.split(','),string2.split(','))

if __name__ == '__main__':
    app.run(debug=True)