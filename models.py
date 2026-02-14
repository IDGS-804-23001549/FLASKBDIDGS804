from flask_sqlalchemy import SQLAlchemy

import datatime


db.SQLAlchemy()
class Alumnos(db_Model):
    _tablename_ = "alumnos"
    id = db.column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apaterno = db.Column(db.String(50))
    email = db.Column(db.String(50))
    create_date = db.Column(db.DataTime, default = datatime.datatime.now)