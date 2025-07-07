print('            👨💻 Banking Management System👨💻 ')  
print('       📚✏Made by:-- ') 
# Importing MySQL connector module to interact with MySQL database
import mysql.connector as m
# Establishing connection with MySQL server
s=m.connect(user='root',host='localhost',passwd='',charset='utf8',auth_plugin='mysql_native_password')
c=s.cursor() 
# Creating the database if it doesn't already exist
c.execute('''create database if not exists banking_management''') 
# Selecting the database to use
c.execute('''use banking_management''')

# Function to create Admin table if it doesn't exist
def Table_for_admins(): 
   c.execute("""create table if not exists Admin(Id int(5)primary key, 
             Name varchar(40),admin_key int(10),Designation varchar(30), 
             Salary_per_month int(8))""")
Table_for_admins()

# Function to create customer-related tables (Loan, Credit Card, FD, etc.)
def Table_for_customers(): 
    c.execute('''create table if not exists Loan( loan_id INT(10)PRIMARY KEY,
              Name varchar(17),     loan_amount INT(7) NOT NULL,     interest_rate DECIMAL(5,2) NOT NULL,
              loan_term INT NOT NULL,     start_date DATE NOT NULL,     end_date DATE NOT NULL,     monthly_payment INT(5) NOT NULL,
              loan_status VARCHAR(20) NOT NULL)''')
    c.execute('''create table if not exists Credit_card(     customer_id INT(10) PRIMARY KEY,
              first_name VARCHAR(15) NOT NULL,     last_name VARCHAR(15) NOT NULL,     date_of_birth DATE NOT NULL,     city VARCHAR(30) NOT NULL,
              state VARCHAR(15) NOT NULL,     account_creation_date DATE NOT NULL,     credit_limit DECIMAL(8,2) NOT NULL,
              current_balance DECIMAL(8,2) NOT NULL)''')
    c.execute('''create table if not exists FD(     fd_id INT(6)PRIMARY KEY,     user_id INT(5) NOT NULL,     Name varchar(30),
              principal_amount DECIMAL(10,2) NOT NULL, interest_rate DECIMAL(5,2) NOT NULL, 
              start_date DATE NOT NULL,     maturity_date DATE NOT NULL,     maturity_amount DECIMAL(10,2) NOT NULL)''') 
    c.execute('''create table if not exists Loan_extras(loan_id int(10),Name varchar(30),     Collateral varchar(100),Loan_type varchar(30))''') 
    c.execute('''create table if not exists Credit_extras(     customer_id int(20),Name varchar(20),Address varchar(30), Phone_number int(11))''')
Table_for_customers()

# Function to insert predefined admin records
def insert_values_for_admin(): 
    c.execute('''insert into admin values(567442,'Mohan', 
               554321334,'S.Bank Manager',95000)''')
    c.execute('''insert into admin values(567487,'Aadvik', 
                564321334,'A. Bank Manager',80000)''')
    c.execute('''insert into admin values(567564,'Aryan', 
                 543554324,'S.Data Handler',65000)''') 
    c.execute('''insert into admin values(454535,'Aditya', 
                564643625,'Data Handler',30000)''')
    c.execute('''insert into admin values(459465,'Amit', 
                473948294,'Data Handler',25000)''')
insert_values_for_admin()

# Function to insert sample loan records
def insert_values_for_loan(): 
    c.execute('''insert into loan values(179632,'Neha', 50000.00, 5.5, 
        3,'2023-01-01','2026-01-01',1500, 'active')''')
    c.execute('''insert into loan values(812343,'Dhruv', 150000.00, 6.0, 
        5,'2023-02-01', '2028-02-01',3500, 'approved')''') 
    c.execute('''insert into loan values(532431,'Shiva',200000.00, 6.5, 
      4,'2023-03-01','2027-03-01',5000,'pending')''')
    c.execute('''insert into loan values(523454,'Khushi', 75000.00, 5.0, 
      3,'2023-04-01','2026-04-01',3000,'active')''')
    c.execute('''insert into loan values(248324,'Arjun',125000.00, 5.8, 
      4,'2023-05-01','2027-05-01',5500,'completed')''') 
    c.execute('''insert into loan values(378194,'Sita', 100000.00, 6.2,
      3, '2023-06-01', '2026-06-01',3000, 'defaulted')''')
insert_values_for_loan()

# Function to insert sample credit card records
def insert_values_for_Credit_card(): 
   c.execute('''insert into Credit_card values(898723, 'Avi', 'Kumar', 
           '1991-11-05', 'Pune', 'Maharashtra','2023-06-01', 55000, 12000)''')
   c.execute('''insert into Credit_card values(111234, 'Rohan', 'Desai', 
         '1987-03-12', 'Kolkata', 'West Bengal', '2023-07-01', 65000, 18000)''') 
   c.execute('''insert into Credit_card values(129342, 'Aarav', 'Mehta', 
         '1993-12-19',  'Ahmedabad', 'Gujarat', '2023-08-01', 75000, 14000)''') 
   c.execute('''insert into Credit_card values(281929, 'Lakshmi', 'Nair', 
            '1989-04-22', 'Thiruvananthapuram', 'Kerala', '2023-09-01', 85000, 22000)''')
   c.execute('''insert into Credit_card values(561283, 'Vikram', 'Rao', 
         '1994-06-30',  'Jaipur', 'Rajasthan',  '2023-10-01', 95000, 27000)''')
insert_values_for_Credit_card() 

# Function to insert fixed deposit records
def insert_into_FD(): 
   c.execute('''insert into FD values(192384, 101, 'Ananya', 100000.00, 5.5, 
            '2021-01-01', '2026-01-01', 117000.00)''') 
   c.execute('''insert into FD values(134242, 102, 'Neha Patel', 150000.00, 6.0, 
             '2022-02-01', '2028-02-01', 201450.00)''') 
   c.execute('''insert into FD values(812832, 103, 'Rahul Verma', 200000.00, 5.8, 
            '2019-03-01', '2027-03-01', 239360.00)''') 
   c.execute('''insert into FD values(912913, 104, 'Priya Singh', 50000.00, 5.0, 
           '2018-04-01', '2026-04-01', 57881.25)''') 
   c.execute('''insert into FD values(612123, 105, 'Advait Reddy', 250000.00, 6.2, 
          '2020-05-01', '2029-05-01', 360687.50)''')
insert_into_FD()

# Function to insert additional information about loans
def insert_values_for_loan_extras(): 
   c.execute('''insert into loan_extras values(179632,'Neha','Car', 
         'House loan')''')        
   c.execute('''insert into loan_extras values(812343,'Dhruv','Jwellery', 
        'Students loan')''') 
   c.execute('''insert into loan_extras values(532431,'Shiva','stock certificates', 
         'Mortgage loans')''') 
   c.execute('''insert into loan_extras values(523454,'Khushi','Null', 
         'Personal loan')''') 
   c.execute('''insert into loan_extras values(248324,'Arjun','Car', 
         'Auto loan')''') 
   c.execute('''insert into loan_extras values(378194,'Sita','Null', 
        'Personal loan')''')
insert_values_for_loan_extras()

# Function to insert additional credit card holder information
def insert_values_for_credit_extras(): 
   c.execute('''insert into credit_extras values(898723,'Avi', 
         '123, Gandhi Road', 98763210)''')
   c.execute('''insert into credit_extras values(111234,'Rohan', 
         '456, Nehru Street',87652109)''') 
   c.execute('''insert into credit_extras values(129342,'Aarav', 
         '789, Tagore Avenue',76541098)''') 
   c.execute('''insert into credit_extras values(281929,'Lakshmi', 
         '321, Patel Nagar',65432187)''') 
   c.execute('''insert into credit_extras values(561283,'Vikram', 
         '987, Rajaji Lane',54321076)''')
insert_values_for_credit_extras() 
# Committing all changes to the database
s.commit()
# Final confirmation message
print('                 ✔  Database Created  ✔') 