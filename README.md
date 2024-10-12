# 📚 School Management System

## 📖 Description
This project is a **School Management System** built using **Python** and **MySQL**, developed as part of an investigatory project for the 12th board exams. The system helps in managing student and teacher data efficiently, including features for attendance and salary updates.

## Key Features:
- 📝 Add, remove, and view student and teacher records
- 📅 Manage class and teacher attendance
- 💰 Update teacher salaries
- 📂 Easy database interaction using MySQL
- 🚀 Getting Started
### Prerequisites
Make sure you have the following installed on your system:

- **Python 3.x**
- **MySQL**
- **MySQL Connector**

##🔧 Installation and Setup
### 1. Clone the repository:

```bash
git clone <repository_url>
cd school-management-system
```
### 2. Install dependencies:

```bash
pip install mysql-connector-python
```
### 3. Set up MySQL:

Open MySQL and create a new database:
```bash
CREATE DATABASE db1;
```
Update the MySQL credentials inside your Python script, if necessary:
```bash
con = mysql.connector.connect(host='localhost', user='root', database='db1', password='System')
```
## 🛠️ How to Run the Project
Open your terminal or command prompt.

Run the Python script:

```bash
python school_management.py
```
Follow the menu prompts to:
**Add, remove, or display students and teachers.**
**Manage attendance records.**
**Update teacher salaries.**

## 🗂️ Project Structure
```bash
school-management-system/
│
├── school_management.py      # Main Python script
├── README.md                 # Documentation
└── requirements.txt          # Dependencies (if any)
```
## 📸 Screenshots
Add screenshots here if you have any!

## 🤝 Contributing
Contributions are welcome!

**Fork the project.
**Create a feature branch: git checkout -b feature-name.**
**Commit changes: git commit -m 'Add feature'.**
**Push to your branch: git push origin feature-name.**
**Create a pull request.**

## Author
Shlok
Feel free to connect with me! 🚀

## ⚠️Disclaimer
This project was built as an investigatory project and is intended for educational purposes only.
