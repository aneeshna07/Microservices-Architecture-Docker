from flask_restful import Resource, Api
from flask import Flask

app = Flask(__name__)
app.secret_key = "multiply"
api = Api(app)

class Multiply(Resource):
    def get(self, number_1:str, number_2:str):
        return int(number_1) * int(number_2)
    
api.add_resource(Multiply, "/api/multiply/<string:number_1>/<string:number_2>")

if __name__ == '__main__':
    app.run(
        debug=True,
        port = 5002,
        host="0.0.0.0"
    )