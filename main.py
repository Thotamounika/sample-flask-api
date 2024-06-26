from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

persons = {
    "Harry": {"age": 21, "gender": "male"},
    "Ron": {"age": 22, "gender": "male"},
    "Hermoine": {"age": 21, "gender": "female"}
}

class HelloWorld(Resource):
    def get(self, name):
        return persons[name]
    
api.add_resource(HelloWorld, "/helloworld/<string:name>")

if __name__ == "__main__":
    app.run(debug=True)