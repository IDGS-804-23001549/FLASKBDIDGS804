from . import maestros
from flask import render_template, request, redirect, url_for, flash
import forms
from models import db, Maestros

@maestros.route("/index")
@maestros.route("/")
def index():
    maestros_list = Maestros.query.all()
    return render_template("maestros/listadoMaes.html", maestros=maestros_list)

@maestros.route('/crear', methods=['GET', 'POST'])
def crear():
    create_form = forms.MaestroForm(request.form)
    if request.method == "POST" and create_form.validate():
        maes = Maestros(
            nombre=create_form.nombre.data,
            apellidos=create_form.apellidos.data,
            especialidad=create_form.especialidad.data,
            email=create_form.email.data
        )
        db.session.add(maes)
        db.session.commit()
        return redirect(url_for("maestros.index"))
    
    return render_template("maestros/crearMaestro.html", form=create_form)

@maestros.route("/detalles", methods=["GET"])
def detalles():
    matricula = request.args.get("id") # En tu HTML usaste 'id' en el link
    maestro = Maestros.query.get_or_404(matricula)
    return render_template("maestros/detalleMaestro.html", maestro=maestro)

@maestros.route('/modificar', methods=['GET', 'POST'])
def modificar():
    matricula = request.args.get('matricula')
    maes = Maestros.query.get_or_404(matricula)
    
    # Si es GET, cargamos el objeto. Si es POST, cargamos lo que envió el usuario
    if request.method == 'GET':
        create_form = forms.MaestroForm(obj=maes)
    else:
        create_form = forms.MaestroForm(request.form)

    if request.method == 'POST' and create_form.validate():
        maes.nombre = create_form.nombre.data
        maes.apellidos = create_form.apellidos.data
        maes.especialidad = create_form.especialidad.data
        maes.email = create_form.email.data
        
        db.session.commit()
        return redirect(url_for('maestros.index'))
    
    # Si hay errores de validación, imprimirlos para saber qué pasa
    if create_form.errors:
        print(create_form.errors)
        
    return render_template('maestros/modificarMaestro.html', form=create_form, matricula=matricula)

@maestros.route('/eliminar', methods=['GET', 'POST'])
def eliminar():
    matricula = request.args.get('id')
    maes = Maestros.query.get_or_404(matricula)
    
    # Creamos la instancia del formulario
    create_form = forms.MaestroForm(obj=maes)
    
    if request.method == 'POST':
        db.session.delete(maes)
        db.session.commit()
        return redirect(url_for('maestros.index'))
    
    # IMPORTANTE: Pasar 'form' al template
    return render_template('maestros/eliminarMaestro.html', maestro=maes, form=create_form)