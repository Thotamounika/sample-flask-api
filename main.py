from flask import Flask, request, abort, jsonify, render_template
from flask_restful import Api, Resource, reqparse
import requests

app = Flask(__name__)
api = Api(app)

shorts_post_args = reqparse.RequestParser()
shorts_post_args.add_argument("title", type=str, help="Title of the short", required = True)
shorts_post_args.add_argument("content", type=str, help="Summary of the news", required = True)
shorts_post_args.add_argument("url", type=str, help="Orginal Source of the news article", required = True)


# shorts = {
#     1: {"title": "India won the T20 world cup", "summary": "India won the world cup with a tough fight in T20.", "srcLink": "http://newsarticle.com"},
#     2: {"title": "Nvidia stocks reached market high", "summary": "Nvidia stocks became the most valuable stocks exceeding the Alphabet stocks", "srcLink": "http://newsarticle.com"},
#     3: {"title": "Self-driving cars Operational in US", "summary": "Now you can go on a rider without a driver. Self-driving cars are operational in US", "srcLink": "http://newsarticle.com"},
# }

shorts = {}

NEWS_API_KEY = '990ebb54198a49c0923eb18c9a9d2cdb' 
NEWS_API_URL = 'https://newsapi.org/v2/top-headlines'

def fetch_news():
    params = {
        'apiKey': NEWS_API_KEY,
        'country': 'in',  
        'category': 'technology'  
    }
    response = requests.get(NEWS_API_URL, params=params)
    if response.status_code == 200:
        news_data = response.json().get('articles', [])
        result = [{'title': article['title'], 'content': article.get('content', 'No content available'), 'url': article['url']} for article in news_data if article.get('content')][:5]
        return result
    else:
        abort(response.status_code, message="Failed to fetch news")

def abort_if_short_id_doesnt_exist(short_id):
    if short_id not in shorts:
        abort(404,message="Short id is not valid..")

def abort_if_short_id_already_exists(short_id):
    if short_id in shorts:
        abort(409,message="Shorts already exist with that ID...")

class Shorts(Resource):
    def get(self, short_id):
        abort_if_short_id_doesnt_exist(short_id)
        return shorts[short_id]
    
    def post(self, short_id):
        abort_if_short_id_already_exists(short_id)
        args = shorts_post_args.parse_args()
        shorts[short_id] = args
        return shorts[short_id], 201
    
    def delete(self, short_id):
        abort_if_short_id_doesnt_exist(short_id)
        del shorts[short_id]
        return '', 204
    
 
class News(Resource):
    def get(self):
        news_data = fetch_news()
        return news_data
    

api.add_resource(Shorts, "/shorts/<int:short_id>")
api.add_resource(News, "/news")


if __name__ == "__main__":
    app.run(debug=True)