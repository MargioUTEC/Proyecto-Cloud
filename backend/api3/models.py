from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from sqlalchemy.dialects.postgresql import ARRAY

database_name = 'uteccine'
database_path = 'postgresql://{}@{}/{}'.format('postgres:123','54.85.151.11:8080',database_name)
    
db = SQLAlchemy()
#Models

def setup_db(app, database_path = database_path):
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    with app.app_context():
        db.create_all()

class Products(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), unique = True)
    price = db.Column(db.Float, default = 0)
    stock = db.Column(db.Integer, default = 0)

    def get_id(self):
        return (self.id)
    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except:
            db.session.rollback()
        finally:
            db.session.close()
    def update(self):
        try:
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()
    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'stock': self.stock
        }

class Promotions(db.Model):
    __tablename__ = 'promotions'
    code = db.Column(db.String(20), primary_key = True)
    is_active = db.Column(db.Boolean, default = False)
    price = db.Column(db.Float, default = 0)

    def get_code(self):
        return (self.code)
    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.code
        except:
            db.session.rollback()
        finally:
            db.session.close()
    def update(self):
        try:
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()
    def format(self):
        return {
            'code': self.code,
            'is_active': self.is_active,
            'price': self.price
        }

class Coupons(db.Model):
    __tablename__ = "coupons"
    code = db.Column(db.String(20), primary_key = True)
    is_active = db.Column(db.Boolean, default = False)
    percentage = db.Column(db.Float, default = 0)
    
    def get_id(self):
        return (self.code)
    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.code
        except:
            db.session.rollback()
        finally:
            db.session.close()
    def update(self):
        try:
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()
    def format(self):
        return {
            'code': self.code,
            'is_active': self.is_active,
            'percentaje': self.percentaje
        }

class Products_Promotions(db.Model):
    __tablename__ = "products_promotions"
    id_p = db.Column(db.Integer, ForeignKey('products.id'), primary_key = True)
    code_p = db.Column(db.String(20), ForeignKey('promotions.code'), primary_key = True)

    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.code
        except:
            db.session.rollback()
        finally:
            db.session.close()
    def update(self):
        try:
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()
    def format(self):
        return {
            'id_products': self.id_p,
            'code_promotions': self.code_p
        }


    
