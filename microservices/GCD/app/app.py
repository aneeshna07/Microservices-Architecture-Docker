from flask_restful import Resource, Api
from flask import Flask
import math

app = Flask(__name__)
app.secret_key = "gcd"
api = Api(app)

class GCD(Resource):
    def get(self, number_1:str, number_2:str):
        return math.gcd(int(number_1), int(number_2))
    
api.add_resource(GCD, "/api/gcd/<string:number_1>/<string:number_2>")

if __name__ == '__main__':
    app.run(
        debug=True,
        port = 5005,
        host="0.0.0.0"
    )