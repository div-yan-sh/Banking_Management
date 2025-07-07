# Banking_Management
A role-based Banking Management System (Python + MySQL) with CLI interface. Features include FD, Loan, and Credit Card management, secure admin authentication, and CRUD operations. Ideal for DBMS projects, showcasing backend logic and SQL integration.
---

## 🚀 Features

- 🔐 **Owner Access**
  - View all admins
  - Add new admins (auto-generate ID & key)
  - Increase salary
  - Update admin designation
  - Delete admin accounts

- 👨‍💼 **Admin Login** (Role-based):
  - `S. Bank Manager`: Full access (FD, Loan, Credit Card)
  - `A. Bank Manager`: Loan & Credit Card only
  - `Data Handler`: FD only

- 🧾 **Customer Login**
  - View & break FD
  - Credit FD amount
  - Debit Credit Card / Loan balance
  - View loan & card details

- ✅ Full **CRUD** functionality
- 📊 Data displayed neatly using **Tabulate**
- 🔐 Admin authentication with **admin_key**
- 🗃️ Sample data pre-filled (no manual entry needed)

---

## ⚙️ Tech Stack

- **Language**: Python 3
- **Database**: MySQL
- **Libraries**:
  - `mysql-connector-python`
  - `tabulate`
  - `random`

---

## 📁 Project Structure 

```bash
📦 Banking-Management-System
├── database.py         # Creates DB, tables & inserts sample data
├── front end.py        # Main CLI logic for all user roles
├── .gitignore          # (optional) to ignore cache/log files
├── LICENSE             # MIT License (for open use)
└── README.md           # You're reading it 😄
```

🧪 How to Run
1- Install dependencies:
   bash
   (pip install mysql.connector,
    pip install tabulate,
    pip install random)
2- Run database setup: 
   python (database.py)
3- Run the app:
   python (front_end.py)
