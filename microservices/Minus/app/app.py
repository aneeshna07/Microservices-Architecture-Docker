from flask_restful import Resource, Api
from flask import Flask

app = Flask(__name__)
app.secret_key = "minus"
api = Api(app)

class Minus(Resource):
    def get(self, number_1:str, number_2:str):
        return int(number_1) - int(number_2)
    
api.add_resource(Minus, "/api/minus/<string:number_1>/<string:number_2>")

if __name__ == '__main__':
    app.run(
        debug=True,
        port = 5001,
        host="0.0.0.0"
    )