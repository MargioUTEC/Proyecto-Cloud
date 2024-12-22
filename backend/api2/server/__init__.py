from flask import(
    Flask,
    abort,
    jsonify,
    request
)

from models import setup_db, User_Data, Users, Rooms, Seatings, Functions

from flask_cors import CORS

def paginate(request, selection):
    information = [data.format() for data in selection]
    current_data = information[:]
    return current_data

def create_app(test_config=None):
    app = Flask(__name__)
    
    setup_db(app)
    cors = CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorizations, true')
        response.headers.add('Access-Control-Allow-Methods', 'GET, PATCH, POST, DELETE, OPTIONS')
        return response
    
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'message': 'Bad request',
            'code': 400
        }),400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'message': 'Resource not found',
            'code': 404
        }),404

    @app.errorhandler(422)
    def not_found(error):
        return jsonify({
            'success': False,
            'message': 'Unprocessable',
            'code': 422
        }),422

    @app.errorhandler(403)
    def not_found(error):
        return jsonify({
            'success': False,
            'message': 'Access denied',
            'code': 403
        }),403


    @app.route('/user', methods=['POST'])
    def create_user():
        error_400 = False
        error_404 = False
        error_422 = False
        try:
            body = request.get_json()
            username = body.get('username', None)
            username_exist = Users.query.filter(Users.username_du == username).one_or_none()
            if username_exist is not None:
                error_400 = True
                abort(400)

            email = body.get('email', None)
            email_exist = User_Data.query.filter(User_Data.email == email).one_or_none()

            if email_exist is not None:
                error_400 = True
                abort(400)

            password = body.get('password', None)
            names = body.get('names', None)
            surnames = body.get('surnames', None)

            if username is None or email is None or password is None or names is None or surnames is None:
                error_422 = True
                abort(422)

            user_data = User_Data(username=username, password=password, email=email, names=names, surnames=surnames)

            user = Users(username_du=username, password_du=password)


            new_user_data = user_data.insert()  # Llamada al método insert() en la instancia user_data
            new_user = user.insert()
            return jsonify({
                'success': True,
                'created_user': new_user
                })
        except Exception as e:
            print(e)
            if error_404:
                abort(404)
            elif error_400:
                abort(400)
            elif error_422:
                abort(422)
            else:
                abort(500)
    
    @app.route('/login', methods=['POST'])
    def login():
        error_403 = False
        error_404 = False
        try:
            body = request.get_json()
            username = body.get('username', None)
            username_exist = Users.query.filter(Users.username_du == username).one_or_none()
            if username_exist is None:
                error_404 = True
                abort(404)

            password = body.get('password', None)
            is_password = Users.query.filter(Users.username_du == username, Users.password_du == password).one_or_none()
            if is_password is None:
                error_403 = True
                abort(403)

            return jsonify({
                'success': True,
                'message': 'Acceso concedido',
                'return': username
                })
        except Exception as e:
            print(e)
            if error_403:
                abort(403)
            elif error_404:
                abort(404)
            else:
                abort(500)
    return app
