from flask import(
    Flask,
    abort,
    jsonify,
    request
)

from models import setup_db, Products, Promotions, Coupons, Products_Promotions

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
    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'message': 'Resource not found',
            'code': 404
        }),404
    
    @app.route('/products', methods=['GET'])
    def get_products():
        selection = Products.query.order_by('id').all()
        products = paginate(request, selection)
        if len(products) == 0:
            abort(404)
        
        return jsonify({
            'success': True,
            'products': products,
            'number_products': len(selection)
            })

    @app.route('/promotions', methods=['GET'])
    def get_promotions():
        selection = Promotions.query.order_by('code').all()
        promotions = paginate(request, selection)
        if len(promotions) == 0:
            abort(404)
        
        return jsonify({
            'success': True,
            'products': promotions,
            'number_products': len(selection)
            })

    @app.route('/coupons', methods=['GET'])
    def get_coupons():
        selection = Coupons.query.order_by('code').all()
        coupons = paginate(request, selection)
        if len(coupons) == 0:
            abort(404)
        
        return jsonify({
            'success': True,
            'products': coupons,
            'number_products': len(selection)
            })
    return app
