# PaySplit – Expense Management System

A web-based expense management application built using **Python and Django**. PaySplit helps users manage their personal expenses and track shared expenses in one place.

## 🚀 Features

- **User Registration & Login** – Secure user authentication.
- **Expense Management** – Add, view, update, and delete expenses.
- **Monthly Expense Calculation** – Calculate expenses for a selected month.
- **Shared Expenses** – Record expenses shared with other people.
- **Expense Tracking** – View total expenses through a dashboard.
- **User Dashboard** – Manage expenses from one place.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web framework |
| HTML5 | Frontend structure |
| CSS3 | Styling and responsive design |
| SQLite | Database (if configured as the project database) |
| Git & GitHub | Version control |

## 📂 Project Structure

```text
PaySplit/
│
├── expenseapp/
│   ├── migrations/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── expense_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── static/
│   └── expenseapp/
│       └── expense.css
│
├── templates/
│   └── expenseapp/
│
├── manage.py
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/sahith-27/PaySplit-Expense-Management.git
```

### 2. Navigate to the project directory

```bash
cd PaySplit-Expense-Management
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install Django

```bash
pip install django
```

If you add a `requirements.txt` file to the repository, you can instead install all project dependencies using:

```bash
pip install -r requirements.txt
```

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Run the development server

```bash
python manage.py runserver
```

### 8. Open the application

Visit:

```text
http://127.0.0.1:8000/
```

## 📸 Screenshots

Add screenshots of your actual application here.

### Home Page
<!-- Add your home page screenshot here -->

### Login Page
<!-- Add your login page screenshot here -->

### Dashboard
<!-- Add your dashboard screenshot here -->

### Expense Management
<!-- Add your expense management screenshot here -->

## 🎯 Project Objective

The main objective of PaySplit is to provide a simple platform for managing personal and shared expenses, helping users organize their spending and understand their monthly expenses.

## 👨‍💻 Developer

**Kukkala Sahith**

GitHub: [sahith-27](https://github.com/sahith-27)

Project Repository: [PaySplit – Expense Management System](https://github.com/sahith-27/PaySplit-Expense-Management)

---

⭐ If you find this project useful, feel free to explore the repository!
