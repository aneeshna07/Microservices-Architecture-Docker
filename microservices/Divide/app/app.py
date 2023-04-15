from flask_restful import Resource, Api
from flask import Flask
import math

app = Flask(__name__)
app.secret_key = "divide"
api = Api(app)

class Divide(Resource):
    def get(self, number_1:str, number_2:str):
        if number_2:
            return round(int(number_1) / (number_2), 3)
        else:
            return "Zero Divison Error!"

    
api.add_resource(Divide, "/api/divide/<string:number_1>/<string:number_2>")

if __name__ == '__main__':
    app.run(
        debug=True,
        port = 5003,
        host="0.0.0.0"
    )