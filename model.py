from extensions import db

class Student(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True, nullable=False)
  email = db.Column(db.VARCHAR(200), unique=True, nullable=False)
  cohort = db.Column(db.String(80), unique=False, nullable=False)
  program = db.Column(db.String(100), unique=False, nullable=False)
  status = db.Column(db.String(80), unique=False, nullable=False)