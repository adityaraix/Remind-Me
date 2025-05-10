# Remind Me Later - Flask API

This is a simple Flask-based API that allows users to set reminders with a date, time, message, and a reminder type (SMS or Email).

## 🔧 Tech Stack
- Python
- Flask
- SQLite (via SQLAlchemy)

## 🚀 Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/Remind-Me.git
   cd Remind-Me
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app:**
   ```bash
   python app.py
   ```

5. **Test the API:**
   Use Postman or `curl` to POST to:
   ```
   POST http://localhost:5000/api/reminders
   ```

   With JSON body:
   ```json
   {
     "date": "2025-05-12",
     "time": "14:00",
     "message": "Doctor's appointment",
     "reminder_type": "Email"
   }
   ```

## ✅ Note
This project only stores reminder data and does not handle actual message delivery.

---

## 📂 Sample API Response
```
{
  "message": "Reminder created successfully"
}
```

---

## 👨‍💻 Author
Aditya Rai
# Remind-Me
