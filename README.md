# Django Polls Application

## 📌 Project Overview
This is a Django-based Polls application that allows authenticated users to create, vote, and view poll results. The project includes authentication, a user-friendly dashboard, and an elegant UI powered by Bootstrap.

## 🛠 Features
- User authentication (Sign up, Login, Logout)
- Dashboard for managing polls
- Create, vote, and view poll results
- Bootstrap-styled UI for better user experience
- Custom user model with email authentication
- Secure voting system with user restrictions

## 📂 Project Structure
```
project_root/
│── polls/                     # Main application
│   ├── migrations/            # Database migrations
│   ├── templates/             # HTML templates
│   ├── static/                # Static files (CSS, JS, images)
│   ├── views.py               # Application logic
│   ├── models.py              # Database models
│   ├── forms.py               # Django forms
│── users/                     # User authentication app
│── templates/                 # Global templates
│── db.sqlite3                  # Database (if using SQLite)
│── manage.py                   # Django management script
│── requirements.txt            # Project dependencies
│── README.md                   # Project documentation
```

## 🚀 Installation & Setup
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/django-polls.git
cd django-polls
```

### 2️⃣ Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Run Migrations
```sh
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create a Superuser (For Admin Access)
```sh
python manage.py createsuperuser
```
Follow the prompts to create an admin user.

### 6️⃣ Run the Development Server
```sh
python manage.py runserver
```
Open your browser and visit: **`http://127.0.0.1:8000/`**

## 🔑 Authentication System
- **Sign Up**: Users can register with their email, name, date of birth, and gender.
- **Login**: Users authenticate using their email and password.
- **Logout**: Users can log out from the system.

## 🎨 UI & Styling
- The UI is styled with **Bootstrap 5** for a modern look.
- Navbar includes **Login, Sign Up, Dashboard** links.
- Poll results are displayed with stylish vote count badges.

## 🏗 Built With
- **Django** - Backend framework
- **Bootstrap 5** - Frontend styling
- **SQLite/PostgreSQL** - Database (depending on setup)

## 🤝 Contributing
Feel free to fork this repository and submit pull requests. Contributions are welcome!

## 📜 License
This project is licensed under the MIT License.

---
### 🎯 Next Steps
- Add **password reset functionality**
- Improve **polls visualization with charts**
- Implement **pagination for dashboard polls**

