from flask_restful import Resource, Api
from flask import Flask

app = Flask(__name__)
app.secret_key = "modulus"
api = Api(app)

class Modulus(Resource):
    def __init__(self):
        self.response = {"status": 400, "message": "No Operation"}

    def get(self, number_1:str, number_2:str):
        if int(number_2):
            return int(number_1) % int(number_2)
        else:
            return "Zero Divison Error!"

api.add_resource(Modulus, "/api/modulus/<string:number_1>/<string:number_2>")

if __name__ == '__main__':
    app.run(
        debug=True,
        port = 5004,
        host="0.0.0.0"
    )