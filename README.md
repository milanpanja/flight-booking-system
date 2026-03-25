# ✈️ Flight Booking System (Flask + PostgreSQL)

A complete backend-based Flight Booking System built using Flask, PostgreSQL, and JWT authentication. This project simulates real-world airline booking operations including user authentication, flight management, and ticket booking.

---

## 🚀 Features

### 🔐 Authentication & Authorization

* User Registration & Login
* Password hashing using Bcrypt
* JWT-based authentication
* Protected routes using middleware

---

### 👤 User Management

* Create and manage user profiles
* Update profile details
* View logged-in user profile
* Admin can create users (optional role-based system)

---

### ✈️ Flight Management

* Add new flights
* Update flight details
* Delete flights
* View all flights
* View single flight details

---

### 📖 Booking System

* Book flights with seat selection
* View user bookings
* Maintain relationship between users and flights

---

## 🛠️ Tech Stack

* **Backend:** Flask (Python)
* **Database:** PostgreSQL
* **ORM:** Flask-SQLAlchemy
* **Authentication:** JWT (Flask-JWT-Extended)
* **Security:** Flask-Bcrypt

---

## 📁 Project Structure

```
Flight Booking System/
│
├── app.py
├── config.py
├── requirements.txt
│
├── models/
│   ├── user_model.py
│   ├── flight_model.py
│   └── booking_model.py
│
├── routes/
│   ├── auth_routes.py
│   ├── flight_routes.py
│   └── booking_routes.py
│
├── templates/
├── static/
└── env/
```

---

## ⚙️ Installation (Linux)

### 1. Clone the repository

```bash
git clone https://github.com/your-username/flight-booking-system.git
cd flight-booking-system
```

### 2. Create virtual environment

```bash
python3 -m venv env
source env/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Database

Update `config.py`:

```python
SQLALCHEMY_DATABASE_URI = "postgresql://username:password@localhost:5432/flight_db"
```

### 5. Run the application

```bash
flask run
```

---

## 🔗 API Endpoints

### 🔐 Auth

* `POST /register`
* `POST /login`
* `GET /profile`
* `PUT /edit-profile`

### ✈️ Flights

* `POST /add-flight`
* `GET /flights`
* `GET /flights/<id>`
* `PUT /flights/<id>`
* `DELETE /flights/<id>`

### 📖 Booking

* `POST /book`
* `GET /my-bookings`

---

## 🔒 Authentication Example

```bash
Authorization: Bearer <your_token>
```

---

## 📊 Database Models

* **User**
* **Flight**
* **Booking**

Relationships:

* One user → many bookings
* One flight → many bookings

---

## 🧪 Testing

* Tested using Postman
* JSON-based API responses

---

## 💡 Future Enhancements

* Payment Integration
* Email Notifications
* Seat Availability System
* Admin Dashboard UI
* React Frontend Integration

---

## 📌 Author

**Milan Panja**
