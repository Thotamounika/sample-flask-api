from flask import Flask, request, abort
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

shorts_post_args = reqparse.RequestParser()
shorts_post_args.add_argument("title", type=str, help="Title of the short", required = True)
shorts_post_args.add_argument("summary", type=str, help="Summary of the news", required = True)
shorts_post_args.add_argument("srcLink", type=str, help="Orginal Source of the news article", required = True)


# shorts = {
#     1: {"title": "India won the T20 world cup", "summary": "India won the world cup with a tough fight in T20.", "srcLink": "http://newsarticle.com"},
#     2: {"title": "Nvidia stocks reached market high", "summary": "Nvidia stocks became the most valuable stocks exceeding the Alphabet stocks", "srcLink": "http://newsarticle.com"},
#     3: {"title": "Self-driving cars Operational in US", "summary": "Now you can go on a rider without a driver. Self-driving cars are operational in US", "srcLink": "http://newsarticle.com"},
# }

shorts = {}

def abort_if_short_id_doesnt_exist(short_id):
    if short_id not in shorts:
        abort(404, "Short id is not valid..")

class Shorts(Resource):
    def get(self, short_id):
        abort_if_short_id_doesnt_exist(short_id)
        return shorts[short_id]
    
    def post(self, short_id):
        args = shorts_post_args.parse_args()
        shorts[short_id] = args
        return shorts[short_id], 201
    
 
api.add_resource(Shorts, "/shorts/<int:short_id>")

if __name__ == "__main__":
    app.run(debug=True)