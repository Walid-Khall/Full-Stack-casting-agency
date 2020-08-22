import os
from flask import (Flask,
                   Response,
                   flash,
                   request,
                   jsonify,
                   abort,
                   render_template,
                   make_response)
from sqlalchemy import exc
import json
from flask_cors import CORS, cross_origin
import requests
from models import setup_db, Movie, Actor
from auth import AuthError, requires_auth
from forms import ActorForm, MovieForm

SECRET_KEY = os.urandom(32)

# app = Flask(__name__)
# setup_db(app)
# CORS(app)


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    setup_db(app)

    CORS(app)

    @app.route('/')
    def welcome():
        return render_template('pages/home.html')

    @app.route('/login', methods=['GET'])
    def login():
        req = requests.get(
            'https://alpha-wal.eu.auth0.com/authorize?audience=Casting&response_type=token&client_id=j1aD0Sft59JsiPnXKfREz1Z37jADpDxN&redirect_uri=https://casting-agency-app-capstone.herokuapp.com/callback')
        return Response(
            req.text,
            status=req.status_code,
            content_type=req.headers['content-type'],
        )

    @app.route('/callback', methods=['GET'])
    def post_login():
        return render_template('pages/home.html')

    @app.route('/movies')
    @requires_auth('get:movies')
    def get_movies(jwt):
        try:
            selection = Movie.query.order_by(Movie.id).all()
            movies = [movie.format() for movie in selection]
            return render_template('pages/movies.html', movies=movies)
        except BaseException:
            abort(404)

    @app.route('/movies/<int:movie_id>')
    @requires_auth('get:movies')
    def get_movie(jwt, movie_id):
        try:
            movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
            movie.format()
            return render_template('pages/show_movie.html', movie=movie)
        except BaseException:
            abort(404)

    @app.route('/actors')
    @requires_auth('get:actors')
    def get_actors(jwt):
        try:
            selection = Actor.query.order_by(Actor.id).all()
            actors = [actor.format() for actor in selection]
            return render_template('pages/actors.html', actors=actors)
        except BaseException:
            abort(404)

    @app.route('/actors/<int:actor_id>')
    @requires_auth('get:actors')
    def get_actor(jwt, actor_id):
        try:
            actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
            actor.format()
            return render_template('pages/show_actor.html', actor=actor)
        except BaseException:
            abort(404)

    # DELETE Movies and Actors endpoints

    @app.route('/movies/<id>/delete')
    @requires_auth('delete:movies')
    def delete_movies(jwt, id):
        try:
            movie = Movie.query.filter(Movie.id == id).one_or_none()
            movie.delete()
            flash('Movies ' + id + ' was successfully deleted!')
            return render_template('pages/home.html')
        except BaseException:
            flash('An error occurred. Movie ' + id + ' could not be deleted.')
            abort(404)

    @app.route('/actors/<id>/delete')
    @requires_auth('delete:actors')
    def delete_actors(jwt, id):
        try:
            actor = Actor.query.filter(Actor.id == id).one_or_none()
            actor.delete()
            flash('Movies ' + id + ' was successfully deleted!')
            return render_template('pages/home.html')
        except BaseException:
            flash('An error occurred. Movie ' + id + ' could not be deleted.')
            abort(404)

    # POST Movies and Actors endpoints----------------------------------------

    @app.route('/movies/create')
    @requires_auth('post:movies')
    def create_movie_form(jwt):
        form = MovieForm()
        return render_template('forms/new_film.html', form=form)

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def post_movies(jwt):
        try:
            new_title = request.form['title']
            new_release = request.form['release']
            movies = Movie(title=new_title, release=new_release)
            movies.insert()
            movies = movies.format()
            flash('Movies ' + new_title + ' was successfully listed!')
            return render_template('pages/home.html')
        except BaseException:
            flash(
                'An error occurred. Actor ' +
                new_title +
                ' could not be listed.')
            abort(400)

    @app.route('/actors/create')
    @requires_auth('post:actors')
    def create_actor_form(jwt):
        form = ActorForm()
        return render_template('forms/new_actor.html', form=form)

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def post_actors(jwt):
        try:
            new_name = request.form['name']
            new_age = request.form['age']
            new_gender = request.form['gender']
            actors = Actor(name=new_name, age=new_age, gender=new_gender)
            actors.insert()
            actors = actors.format()
            flash('Actor ' + new_name + ' was successfully listed!')
            return render_template('pages/home.html')
        except BaseException:
            flash(
                'An error occurred. Actor ' +
                new_name +
                ' could not be listed.')
            abort(400)

    # PATCH Movies and Actors endpoints---------------------------------------

    @app.route('/movies/<int:movie_id>/patch')
    @requires_auth('patch:movies')
    def patch_movie_form(jwt, movie_id):
        form = MovieForm()
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
        movie = movie.format()
        return render_template('forms/edit_movie.html', form=form, movie=movie)

    @app.route('/movies/<int:movie_id>/patch', methods=['POST'])
    @requires_auth('patch:movies')
    def update_movies(jwt, movie_id):
        new_title = request.form['title']
        new_release = request.form['release']
        try:
            selection = Movie.query.filter(Movie.id == movie_id).all()
            for movies in selection:
                movies.title = new_title
                movies.release = new_release
            movies.update()
            movies = movies.format()
            flash('Movie was successfully updated!')
            return render_template('pages/home.html')
        except BaseException:
            flash('An error occurred. Movie  could not be update.')
            abort(400)

    @app.route('/actors/<int:actor_id>/patch')
    @requires_auth('patch:actors')
    def patch_actor_form(jwt, actor_id):
        form = ActorForm()
        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
        actor = actor.format()
        return render_template('forms/edit_actor.html', form=form, actor=actor)

    @app.route('/actors/<id>/patch', methods=['POST'])
    @requires_auth('patch:movies')
    def update_actors(jwt, id):
        new_name = request.form['name']
        new_age = request.form['age']
        new_gender = request.form['gender']
        try:
            selection = Actor.query.filter(Actor.id == id).all()
            for actors in selection:
                actors.name = new_name
                actors.age = new_age
                actors.gender = new_gender
            actors.update()
            actors = actors.format()
            flash('Actor was successfully updated!')
            return render_template('pages/home.html')
        except BaseException:
            flash('An error occurred. Movie  could not be updated.')
            abort(404)

    # Error Handling
    '''
    Example error handling for unprocessable entity
    '''

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    # -------------------------------- done -----------------------------

    @app.errorhandler(404)
    def resource_not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    @app.errorhandler(405)
    def not_allowd(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "method not allowd"
        }), 405

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "internal server error"
        }), 500

    @app.errorhandler(409)
    def server_error(error):
        return jsonify({
            "success": False,
            "error": 409,
            "message": "duplicate_resource"
        }), 409

    @app.errorhandler(403)
    def server_error(error):
        return jsonify({
            "success": False,
            "error": 403,
            "message": "forbidden"
        }), 403

    '''
    @TODO implement error handler for AuthError
        error handler should conform to general task above
    '''

    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify({
            'code': 'invalid_header',
            'description': 'Authorization malformed.'
        }), 401

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
