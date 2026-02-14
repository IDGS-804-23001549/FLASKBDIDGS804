from wtforms import Form

from wtforms import StringField, PasswordField, EmailField, BooleanField, IntegerField, RadioField
from wtforms import validators

class UserForm(Form):
    id = IntegerField("id", [
        validators.DataRequired(message = "El campo es requerido")
    ])
    nombre = StringField("Nombre", [
        validators.DataRequired(message = "El campo es requerido")
    ])
    apaterno = StringField("apaterno", [
        validators.DataRequired(message = "El campo es requerido")
    ])
    email = EmailField("email", [
        validators.Email(message = "Ingrese correo valido")
    ])