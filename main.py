import os
from flask import Flask, request, jsonify
from extensions import db, migrate
from model import Student

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

db.init_app(app)
migrate.init_app(app, db)

@app.route('/register', methods=['POST'])
def register():
  data = request.get_json()
  existing_student_mail = Student.query.filter_by(email=data['email'].lower()).first()
  existing_student_name = Student.query.filter_by(name=data['name'].lower()).first()

  if existing_student_mail or existing_student_name:
    return jsonify({'error': 'This account is already existing'}), 400
  
  # checking empty values
  for key, value in data.items():
    if value == '':
      return jsonify({'error': f'{key} is empty'}), 400
    
  student = Student(name=data['name'].lower(), email=data['email'].lower(), cohort=data['cohort'].lower(), program=data['program'].lower())
  db.session.add(student)
  db.session.commit()
  return jsonify({'message': 'Student is already created'}), 201

@app.route('/checkin', methods=['POST'])
def checkin():
  pass

@app.route('/checkout', methods=['POST'])
def checkout():
  pass

@app.route('/status', methods=['POST'])
def status():
  pass

if __name__ == '__main__':
  with app.app_context():
    db.create_all()

  app.run(debug=True)