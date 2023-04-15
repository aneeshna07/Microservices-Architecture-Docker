from flask_restful import Api
from flask import Flask, render_template, request, flash

import requests

app = Flask(__name__)
app.secret_key = "microservices"
api = Api(app)

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
            url = "http://microservices-add-service-1:5000/api/add/"
       
        elif operation == 'minus':
            url = "http://microservices-minus-service-1:5001/api/minus/"

        elif operation == 'multiply':
            url = "http://microservices-multiply-service-1:5002/api/multiply/"

        elif operation == 'divide':
            url = "http://microservices-divide-service-1:5003/api/divide/"

        elif operation == 'modulus':
            url = "http://microservices-modulus-service-1:5004/api/modulus/"

        elif operation == 'gcd':
            url = "http://microservices-gcd-service-1:5005/api/gcd/"

        else:
            url = "http://microservices-equals-service-1:5006/api/equals/"

        url += str(number_1) + "/" + str(number_2)

        print(url)
        response = requests.get(url)
        print(response)
        if response.status_code == 200: 
            flash("Operation Success!")
            if operation == 'equals':
                result = response.text.strip()

            else:
                try:
                    result = float(response.text.strip())
                except Exception:
                    flash(response.text.strip())
                    return render_template('index.html')

        else:
            flash("Operation Failure!")
            return render_template('index.html')
        
        flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')
        
    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port = 8000,
        host="0.0.0.0"
    )