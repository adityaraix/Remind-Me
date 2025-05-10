from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, Reminder
import os

app = Flask(__name__)
base_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def home():
    return jsonify({"message": "Reminder API is running!"})

@app.route('/api/reminders', methods=['POST'])
def create_reminder():
    data = request.get_json()
    required_fields = ['date', 'time', 'message', 'reminder_type']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400

    reminder = Reminder(
        date=data['date'],
        time=data['time'],
        message=data['message'],
        reminder_type=data['reminder_type']
    )

    db.session.add(reminder)
    db.session.commit()

    return jsonify({'message': 'Reminder created successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)
