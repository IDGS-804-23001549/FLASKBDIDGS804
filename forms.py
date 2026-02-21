from wtforms import Form, StringField, IntegerField, EmailField
from wtforms.validators import DataRequired, Length, NumberRange, Email, Optional
from wtforms import validators

class UserForm(Form):

    id = IntegerField(
        "id",
        [
            Optional(), # <--- Agrega esto primero
            validators.number_range(min=1, max=20, message="valor no valido")
        ]
    )

    nombre = StringField(
        "Nombre",
        [
            DataRequired(message="El nombre es obligatorio"),
            Length(min=2, max=50, message="El nombre debe tener entre 2 y 50 caracteres")
        ]
    )

    apellido = StringField(
        "Apellido",
        [
            DataRequired(message="El apellido es obligatorio"),
            Length(min=2, max=200, message="El apellido debe tener entre 2 y 50 caracteres")
        ]
    )

    email = EmailField(
        "Email",
        [
            DataRequired(message="El correo es obligatorio"),
            Email(message="Ingrese un correo válido")
        ]
    )

    telefono = StringField(
        "Telefono",
        [
            DataRequired(message="El telefono es requerido")
        ]
    )