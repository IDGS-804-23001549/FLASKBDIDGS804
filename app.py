from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask import g
import forms
from flask_migrate import Migrate
from models import db, Alumnosdb


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db.init_app(app)
migrate = Migrate(app, db)
# csrf = CSRFProtect()

@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():
    create_form = forms.UserForm(request.form)
    #tem= Alumnos.query('select * from alumnos')
    alumno = Alumnosdb.query.all()
      
    return render_template('index.html', form=create_form, alumnos=alumno)

@app.route('/alumnos', methods=['GET', 'POST'])
def alumnos_view():
    create_form = forms.UserForm(request.form)

    if request.method == "POST" and create_form.validate():
        alum = Alumnosdb(
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

@app.route("/detalles", methods=["GET", "POST"])
def detalles():
    create_form = forms.UserForm(request.form)
    if request.method == "GET":
        id = request.args.get("id")

        alum1 = db.session.query(Alumnosdb).filter(Alumnosdb.id == id).first()

        id = request.args.get("id")
        nombre = alum1.nombre
        apellido = alum1.apellido
        email = alum1.email
        telefono = alum1.telefono

    return render_template("detalle.html", nombre=nombre, apellido=apellido, email=email, telefono=telefono)

@app.route('/modificar', methods=['GET', 'POST'])
def modificar():
    create_form = forms.UserForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        alum1 = db.session.query(Alumnosdb).filter(Alumnosdb.id==id).first()
        create_form.id.data=request.args.get('id')
        create_form.nombre.data = alum1.nombre
        create_form.apellido.data=alum1.apellido
        create_form.email.data=alum1.email
        create_form.telefono.data=alum1.telefono
    
    if request.method == 'POST':
        id = request.args.get('id')
        alum1 = db.session.query(Alumnosdb).filter(Alumnosdb.id==id).first()
        alum1.id=id
        alum1.nombre=create_form.nombre.data
        alum1.apellido= create_form.apellido.data
        alum1.email = create_form.email.data
        alum1.telefono = create_form.telefono.data
        db.session.add(alum1)
        db.session.commit()
        return redirect(url_for('index'))
    
    return render_template('modificar.html', form=create_form)

@app.route('/eliminar', methods=['GET', 'POST'])
def eliminar():
    create_form = forms.UserForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        alum1 = db.session.query(Alumnosdb).filter(Alumnosdb.id==id).first()
        create_form.id.data=request.args.get('id')
        create_form.nombre.data = alum1.nombre
        create_form.apellido.data=alum1.apellido
        create_form.email.data=alum1.email
        create_form.telefono.data=alum1.telefono
    if request.method == 'POST':
        id = create_form.id.data
        alum = Alumnosdb.query.get(id)
        db.session.delete(alum)
        db.session.commit()
        return redirect(url_for('index'))
    
    return render_template('eliminar.html', form=create_form)

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404
    
if __name__ == '__main__':
    # csrf.init_app(app)
    # db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True)