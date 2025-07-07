# Import required modules
import mysql.connector as m  # MySQL connector for DB access
from tabulate import tabulate  # For pretty-printing tables
import random  # To generate random IDs or keys

# Welcome message
print('         💻 Welcome to the Metropolitan Bank💻 ')

# Connect to the MySQL database
s = m.connect(user='root', host='localhost', passwd='', database='banking_management', auth_plugin='mysql_native_password')
c = s.cursor()

# -----------------------------------------------
# 🔐 OWNER & ADMIN FUNCTIONS
# -----------------------------------------------

def display_admins():
    """Show all admin records."""
    c.execute('SELECT * FROM Admin')
    admins = c.fetchall()
    headers = ('Id', 'Name', 'admin_key', 'Designation', 'Salary_per_month')
    print(tabulate(admins, headers=headers, tablefmt='fancy_grid'))

def increase_salary():
    """Increase salary for a specific admin by ID."""
    Id = int(input('Id= '))
    incr = int(input('Increase salary by= '))
    c.execute("UPDATE Admin SET Salary_per_month = Salary_per_month + %s WHERE Id = %s", (incr, Id))
    s.commit()
    print('Updated successfully')
    display_admins()

def update_designation():
    """Update admin designation."""
    Id = int(input("Admin's Id= "))
    print('''Choose the designation --> 
             1. S.Bank Manager  
             2. A.Bank Manager  
             3. Data Handler''')
    ud = int(input('Enter your choice--> '))
    if ud == 1:
        new_designation = 'S.Bank Manager'
    elif ud == 2:
        new_designation = 'A. Bank Manager'
    elif ud == 3:
        new_designation = 'Data Handler'
    else:
        print('Invalid choice')
        return
    c.execute("UPDATE Admin SET Designation = %s WHERE Id = %s", (new_designation, Id))
    s.commit()
    print('Updated successfully')
    display_admins()

def add_new_admin():
    """Add a new admin with random ID and admin key."""
    Id = random.randint(100000, 999999)
    name = input("Enter Name= ")
    admin_key = random.randint(1000000000,9999999999)
    designation = input("Enter Designation= ")
    salary = int(input("Enter Salary per month= "))
    c.execute("INSERT INTO Admin (Id, Name, admin_key, Designation, Salary_per_month) VALUES (%s, %s, %s, %s, %s)", (Id, name, admin_key, designation, salary))
    s.commit()
    print(f'New admin added successfully with ID: {Id} and admin_key: {admin_key}')
    display_admins()

def delete_admin():
    """Delete an admin by ID."""
    Id = int(input("Enter the Id of the admin to delete= "))
    c.execute("DELETE FROM Admin WHERE Id = %s", (Id,))
    s.commit()
    print('Admin deleted successfully')
    display_admins()

def authenticate_admin():
    """Verify admin ID and key, return designation if valid."""
    admin_id = int(input("Enter your ID: "))
    admin_key = int(input("Enter your admin key: "))
    c.execute("SELECT Designation FROM Admin WHERE Id = %s AND admin_key = %s", (admin_id, admin_key))
    admin = c.fetchone()
    if admin:
        return admin[0]  # return designation
    else:
        print("Invalid credentials.")
        return None

# -----------------------------------------------
# 🎛️ ADMIN PANELS BASED ON DESIGNATION
# -----------------------------------------------

def admin_menu(designation):
    """Admin menu with access based on designation (role)."""
    while True:
        print("\nWelcome to the Admin Panel")
        print("Your Designation:", designation)
        if designation == 'S.Bank Manager':
            print('''Choose your task-->
1. View/Edit FD
2. View/Edit Loan
3. View/Edit Credit Card
4. Add FD Customer
5. Delete FD Customer
6. Add Credit Card Customer
7. Delete Credit Card Customer
8. Add Loan Customer
9. Delete Loan Customer
0. Go Back''')
        elif designation == 'A. Bank Manager':
            print('''Choose your task-->
1. View/Edit Loan
2. View/Edit Credit Card
3. Add Credit Card Customer
4. Delete Credit Card Customer
5. Add Loan Customer
6. Delete Loan Customer
0. Go Back''')
        elif designation == 'Data Handler':
            print('''Choose your task-->
1. View/Edit FD
2. Add FD Customer
3. Delete FD Customer
0. Go Back''')

        choice = input("Enter your choice: ")

        # Handle each designation's permissions
        # Calls to view_edit_table, add, delete methods here...
        # (I've shortened this part to avoid spamming here, but it's in your original code)

# -----------------------------------------------
# 🧾 CUSTOMER MENUS FOR FD, LOANS, CREDIT CARDS
# -----------------------------------------------

def customer_menu():
    """Main menu for customer to access FD, Loan, or Credit Card."""
    while True:
        print('''\nCustomer Menu:
1. Login for FD
2. Login for Credit Card
3. Login for Loan
0. Go Back''')
        choice = input("Enter your choice: ")
        # Handle access to each customer section...

# -----------------------------------------------
# 🏁 MAIN MENU: OWNER, ADMIN, CUSTOMER
# -----------------------------------------------

def main_menu():
    """Start menu for owner, admin, or customer login."""
    while True:
        print('''\nMain Menu:
1. Login as Owner
2. Login as Admin
3. Login as Customer
0. Exit''')
        choice = input("Enter your choice: ")
        # Handle login logic...

# Entry point of program
if __name__ == "__main__":
    main_menu()

# Close the database connection at the end
s.close()
