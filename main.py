import os
from flask import Flask, request, jsonify
from extensions import db
from model import Student

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

db.init_app(app)

@app.route('/register', methods=['POST'])
def register():
  data = request.get_json()
  existing_student = Student.query.filter_by(email=data['email']).first()

  if existing_student:
    return jsonify({'error': 'This account is already existing'}), 400
  
  # checking empty values
  for key, value in data.items():
    if value == '':
      return jsonify({'error': f'{key} is empty'}), 400
    
  student = Student(name=data['name'].lower(), mail=data['mail'].lower(), cohort=data['cohort'].lower(), program=data['program'].lower(), status=data['status'].lower())
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