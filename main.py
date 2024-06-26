from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

shorts = {
    1: {"title": "India won the T20 world cup", "summary": "India won the world cup with a tough fight in T20."},
    2: {"title": "Nvidia stocks reached market high", "summary": "Nvidia stocks became the most valuable stocks exceeding the Alphabet stocks"},
    3: {"title": "Self-driving cars Operational in US", "summary": "Now you can go on a rider without a driver. Self-driving cars are operational in US"},
}

class Shorts(Resource):
    def get(self, short_id):
        return shorts[short_id]
    
api.add_resource(Shorts, "/shorts/<int:short_id>")

if __name__ == "__main__":
    app.run(debug=True)