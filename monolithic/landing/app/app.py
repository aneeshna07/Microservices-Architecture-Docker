from flask import Flask, render_template, request, flash, url_for

import requests
import os
import math

app = Flask(__name__)
app.secret_key = "monolithic"

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        try:
            number_1, number_2 = int(request.form.get('first')), int(request.form.get('second'))
        except:
            flash("Invalid Operands!")
            return render_template('index.html')

        operation = request.form.get('operation')
        if operation == 'add':
            result = number_1 + number_2

        elif operation == 'minus':
            result = number_1 - number_2

        elif operation == 'multiply':
            result = number_1 * number_2

        elif operation == 'divide':
            if number_2:
                result = round(number_1 / number_2, 3)
            else:
                flash("Zero Division Error!")
                return render_template('index.html')

        elif operation == 'gcd':
            result = math.gcd(number_1, number_2)

        elif operation == 'modulus':
            if number_2:
                result = round(number_1 % number_2, 3)
            else:
                flash("Zero Division Error!")
                return render_template('index.html')

        else:
            result = (number_1 == number_2)

        flash(f'The Result of the Operation {operation} on {number_1} and {number_2} is {result}')
        
    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=8001,
        host="0.0.0.0"
    )