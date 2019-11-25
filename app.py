# Package Imports
import sqlite3
import re

try:
    # DB Connection
    connection = sqlite3.connect("cdirectory.db")
    # Cursor Initiation
    cursor = connection.cursor()
except:
    print("Database Connection Failed.")

# Flags and Declarations
keep_active_flag = True

# Regex Patterns
yes_no = '[YNyn]'
operation_pattern = '^(ADD|DEL|add|del|SHOW|show)$'

# Create Table Query
create_cd_table = """
CREATE TABLE cdirectory (
entry_number INTEGER PRIMARY KEY,
fname VARCHAR(20),
lname VARCHAR(30),
telephone DATE);
"""

# Create Table
try:
    cursor.execute(create_cd_table)
except:
    print("Using the Contact Directory Database")

while(keep_active_flag):

    # Add Another Record
    add_another_flag = input("Continue to Console Contact Directory? (y/n) ")

    # Repeat Operation Loop
    if (re.match(yes_no, add_another_flag) and add_another_flag != None):
        if (add_another_flag.lower() == 'y'):
            operation = input("Add or Delete record? (ADD/DEL/SHOW) ")
            # Add or Delete Loop
            if(re.match(operation_pattern, operation) and operation != None):
                if(operation.lower() == 'add'):
                    try:
                        # Input Record
                        name = input("Enter a name: ")
                        phone_number = input("Enter the phone number: ")

                        cursor.execute("select * from cdirectory;")

                    except:
                        print("No Database.")
                elif(operation.lower() == 'del'):
                    print("del")
                elif(operation.lower() == 'show'):
                    try:
                        cursor.execute("select * from cdirectory;")
                        full_list = cursor.fetchall()
                        if (len(full_list) == 0):
                            print("No Records")
                        else:
                            print("All Records:")
                            for item in full_list:
                                print(item)
                    except:
                        print("No Database.")
            else:
                print("No such operation.")
        elif (add_another_flag.lower() == 'n'):
            print("Thank you for choosing to use this application.")
            break
    else:
        print("Invalid Entry.")

connection.commit()
connection.close()
