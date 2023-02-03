from auth.auth import auth
from credentials import *
from flask import Flask, redirect, render_template, request, url_for
from flask_bootstrap import Bootstrap5
from models import db
from flask_login import LoginManager
from models import User


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'topsecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{usuario}:{password}@{endpoint}:{puerto}/{nombre_db}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

bootstrap = Bootstrap5(app)
login_manager = LoginManager()
login_manager.init_app(app)
db.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

# loginMgr = LoginManager(app)
# loginMgr.init_app(app)

app.register_blueprint(auth, url_prefix = "")


if __name__=='__main__':
    app.run(debug=True, port=5000)

