from datetime import datetime

import pytz
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()
ma = Marshmallow()

tz = pytz.timezone('America/Bogota')

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(30),nullable = False)
    password = db.Column(db.Text)

    def __repr__(self) -> str:
        return super().__repr__()
    
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
 
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_fk = True

class Evento(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    nombre = db.Column(db.Text)
    categoria = db.Column(db.Text)
    lugar = db.Column(db.Text)
    direccion = db.Column(db.Text)
    fecha_inicio = db.Column(db.TIMESTAMP(timezone=False))
    fecha_fin = db.Column(db.TIMESTAMP(timezone=False))
    modo = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User", backref="eventos")
    
    def to_dict(self):
        return {
            'id' : self.id,
            'nombre' : self.nombre,
            'categoria' : self.categoria,
            'lugar' : self.lugar,
            'direccion' : self.direccion,
            'fecha_inicio' : self.fecha_inicio,
            'fecha_fin' : self.fecha_fin,
            'modo' : self.modo,
            'user_id' : self.user_id,
            'user' : self.user,
        }

class EventoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Evento
        include_fk = True
