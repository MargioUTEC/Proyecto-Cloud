from flask_sqlalchemy import SQLAlchemy
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

class Movies(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(50), unique=True)
    year = db.Column(db.Integer, nullable = False)
    gender = db.Column(ARRAY(db.String(100)), nullable = False)
    language = db.Column(ARRAY(db.String(100)), nullable = False)
    classification = db.Column(ARRAY(db.String(100)), nullable = False)
    duration = db.Column(db.Float, nullable = False)
    description = db.Column(db.String(200), nullable = False)

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
            'year': self.year,
            'gender': self.gender,
            'language': self.language,
            'classification': self.classification,
            'duration': self.duration,
            'description': self.description
        }

