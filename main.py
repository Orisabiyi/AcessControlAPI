from flask import Flask
from extensions import db

app = Flask(__name__)
db.init_app(app)

@app.route('/register', methods=['POST'])
def register():
  pass

@app.route('/checkin', methods=['POST'])
def checkin():
  pass

@app.route('/checkout', methods=['POST'])
def checkout():
  pass

@app.route('/status', methods=['POST'])
def status():
  pass