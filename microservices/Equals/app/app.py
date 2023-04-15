from flask_restful import Resource, Api
from flask import Flask

app = Flask(__name__)
app.secret_key = "equals"
api = Api(app)

class Equals(Resource):
    def get(self, number_1:str, number_2:str):
        return number_1 == number_2

api.add_resource(Equals, "/api/equals/<string:number_1>/<string:number_2>")

if __name__ == '__main__':
    app.run(
        port = 5006,
        debug=True,
        host="0.0.0.0"
    )