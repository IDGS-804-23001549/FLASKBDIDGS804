from . import maestros
from flask import render_template, request, redirect, url_for
import forms
from maestros.routes import maestros, maestros
from models import db
from models import Alumnosdb, Maestros

@maestros.route('/perfil/<nombre>')
def perfil(nombre):
    return f"perfil de {nombre}"

@maestros.route("/maestros", methods = ['GET', 'POST'])
@maestros.route("/index")
def index():
    create_form = forms.UserForm(request.form)
    maestros = Maestros.query.all()
    return render_template("maestros/listadoMaes.html", form=create_form, maestros=maestros)

@maestros.route('/maestros', methods=['GET', 'POST'])
def alumnos_view():
    create_form = forms.MaestroForm(request.form)

    if request.method == "POST" and create_form.validate():
        maes = Maestros(
            nombre=create_form.nombre.data,
            apellido=create_form.apellido.data,
            email=create_form.email.data,
            telefono = create_form.telefono.data
        )
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for("index"))
    else:
        print(create_form.errors)

    return render_template("Alumnos.html", form=create_form)
