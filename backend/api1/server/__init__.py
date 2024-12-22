from flask import(
    Flask,
    abort,
     jsonify,
    request
)

from models import setup_db, Movies

from flask_cors import CORS


MOVIES_PAGE=5

def paginate(request, selection, isDecendent):
    if isDecendent:
        start = len(selection) - MOVIES_PAGE
        end = len(selection)
    else:
        page = request.args.get('page',1,type=int)
        start = (page - 1)*MOVIES_PAGE
        end = start + MOVIES_PAGE
    movies = [movie.format() for movie in selection]
    current_movies = movies[:]
    return current_movies

def create_app(test_config=None):
    app = Flask(__name__)

    setup_db(app)
    cors = CORS(app, resources={r"/*": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorizations, true')
        response.headers.add('Access-Control-Allow-Methods', 'GET, PATCH, POST, DELETE, OPTIONS')
        return response

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'message': 'Resource not found',
            'code': 404
        }),404

    @app.route('/movies', methods=['GET'])
    def get_movies():
        selection = Movies.query.order_by('id').all()
        movies = paginate(request,selection,False)
        if len(movies) == 0:
            abort(404)
        return jsonify({
            'success': True,
            'movies': movies,
            'number_movies': len(selection)
            })

    @app.route('/movie/<name>', methods=['GET'])
    def get_movie(name):

        movie = Movies.query.filter(Movies.name == name).one_or_none()
        if movie is None:
            abort(404)
        movie_info = movie.format()
        return jsonify({
            'success': True,
            'movie_info': movie_info
        })


    return app

