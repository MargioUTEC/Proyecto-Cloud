from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from sqlalchemy.dialects.postgresql import ARRAY

from datetime import time

database_name = 'uteccine'
database_path = 'postgresql://{}@{}/{}'.format('postgres:123', '54.85.151.11:8080', database_name)

db = SQLAlchemy()
#Models

def setup_db(app, database_path = database_path):
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    with app.app_context():
        db.create_all()

class User_Data(db.Model):
    __tablename__ = "user_data"
    username = db.Column(db.String(20), primary_key = True)
    password = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(20), unique = True)
    names = db.Column(db.String(30), nullable = False)
    surnames = db.Column(db.String(30), nullable = False)

    def get_username(self):
        return (self.username)
    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.username
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
            'username': self.username,
            'password': self.password,
            'email': self.email,
            'names': self.names,
            'surnames': self.surnames
        }
class Users(db.Model):
    __tablename__ = "users"
    username_du = db.Column(db.String(20), ForeignKey('user_data.username'), primary_key = True)
    password_du = db.Column(db.String(20), nullable = False)

    def get_username_du(self):
        return (self.username_du)
    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.username_du
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
            'username': self.username_du,
            'password': self.password_du
        }

class Rooms(db.Model):
    __tablename__ = 'rooms'
    id = db.Column(db.String(3), primary_key = True)
    current_capacity = db.Column(db.Integer, default = 0)
    total_capacity = db.Column(db.Integer, default = 60)
    
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
            'current_capacity': self.current_capacity,
            'total_capacity': self.total_capacity
            }

class Seatings(db.Model):
    __tablename__ = 'seatings'
    id_r = db.Column(db.String(3), ForeignKey('rooms.id'), primary_key = True)
    numero = db.Column(db.Integer, nullable = False)
    fila = db.Column(db.String(1), nullable = False)
    its_busy = db.Column(db.Boolean, default = False)

    def get_id(self):
        return (self.id_r)
    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.id_r
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
            'id_r': self.id_r,
            'numero': self.numero,
            'fila': self.fila,
            'its_busy': self.its_busy
        }


class Functions(db.Model):
    __tablename__ = 'functions'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    id_r = db.Column(db.String(3), ForeignKey('rooms.id'), nullable = False)
    movie = db.Column(db.String(50), nullable = False)
    hour = db.Column(db.Time, nullable = False)
    date = db.Column(db.String(4), nullable = False)

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
            'hall': self.hall,
            'movie': self.movie,
            'hour': self.hour,
            'date': self.date
        }


