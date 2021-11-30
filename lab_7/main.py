from flask import Flask
from flask_restful import Resource, Api
from services.repository import *

app = Flask(__name__)
api = Api(app)

class GetLinks(Resource):
    def get(self):
        return get_links()

class GetMovies(Resource):
    def get(self):
        return get_movies()

class GetRatings(Resource):
    def get(self):
        return get_ratings()

class GetTags(Resource):
    def get(self):
        return get_tags()

class HelloWorld(Resource):
    def get(self):
        return get_tags(), get_ratings(), get_links(), get_movies()



api.add_resource(GetLinks,'/link')
api.add_resource(GetRatings,'/ratings')
api.add_resource(GetMovies,'/movies')
api.add_resource(GetTags,'/tags')

if __name__=='__main__':
    app.run(debug = True)