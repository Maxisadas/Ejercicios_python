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

if __name__ == '__main__':
    app.run(debug=True)