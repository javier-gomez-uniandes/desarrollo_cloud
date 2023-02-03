from auth.forms import *
from flask import Blueprint, redirect, render_template, url_for, session, flash
from flask_login import login_user, logout_user
from models import *

auth = Blueprint("auth",
                 __name__,
                 static_folder="static",
                 template_folder="templates")

@auth.route("/home", methods=['GET', 'POST'])
@auth.route("/",methods=['GET', 'POST'])
def home():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user:
            print(user.id)
            if user.password == form.password.data:
                session['user_id'] = user.id
                return redirect(url_for('auth.eventos', user_id = int(user.id), _external = True))
    return render_template("home.html", form = form, title = 'INICIO')

@auth.route("/registrarse", methods=['GET', 'POST'])
def registrarse():
    form = RegistrarseForm()
    if form.validate_on_submit():
        usuario = User(email = form.email.data,
                       password = form.password.data)
        db.session.add(usuario)
        db.session.commit()
        return redirect(url_for('auth.home'))
    
    return render_template("registrarse.html", form = form, title = 'REGISTRARSE')

@auth.route("/eventos", methods = ['GET', 'POST'])
def eventos():   
    resultados = Evento.query.filter_by(user_id = session['user_id']).all()
    resultados_list = [s.to_dict() for s in resultados] 
    return render_template("eventos.html", title = 'EVENTOS', rows = resultados_list)

@auth.route("/crear_evento", methods = ['GET', 'POST'])
def crear_evento():
    form = CrearEventoForm()
    if form.validate_on_submit():
        nuevo_evento = Evento(nombre = form.nombre.data,
                              categoria = form.categoria.data,
                              lugar = form.lugar.data,
                              direccion = form.direccion.data,
                              fecha_inicio = form.fecha_inicio.data,
                              fecha_fin = form.fecha_fin.data,
                              modo = form.modo.data,
                              user_id = session['user_id'])
        db.session.add(nuevo_evento)
        db.session.commit()
        return redirect(url_for('auth.eventos'))
    return render_template("crear_eventos.html", form = form, title = 'EVENTOS', accion = 'CREAR')

@auth.route("/<int:evento_id>/modificarEvento", methods = ['GET', 'POST'])
def modificarEvento(evento_id):
    evento_modificar = Evento.query.filter_by(id = evento_id).first()
    form = CrearEventoForm(obj = evento_modificar)
    if form.validate_on_submit():
        evento_modificar.nombre = form.nombre.data
        evento_modificar.categoria = form.categoria.data
        evento_modificar.lugar = form.lugar.data
        evento_modificar.direccion = form.direccion.data
        evento_modificar.fecha_inicio = form.fecha_inicio.data
        evento_modificar.fecha_fin = form.fecha_fin.data
        evento_modificar.modo = form.modo.data

        db.session.commit()
        return redirect(url_for('auth.eventos'))
    return render_template("crear_eventos.html", form = form, title = 'EVENTOS', accion = 'MODIFICAR')

@auth.route("/<int:evento_id>/borrarEvento", methods = ['GET', 'POST'])
def borrarEvento(evento_id):
    evento_borrar = Evento.query.filter_by(id = evento_id).first()
    db.session.delete(evento_borrar)
    db.session.commit()
    flash(f'Eliminado exitosamente el id: {evento_borrar.id}')
    return redirect(url_for('auth.eventos'))

@auth.route('/logout')
def logout():
    logout_user()
    session.clear()
    return redirect(url_for('auth.home'))


