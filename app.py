# Package Imports
import sqlite3
import re

try:
    # DB Connection
    connection = sqlite3.connect("CCDirectory.db")
    # Cursor Initiation
    cursor = connection.cursor()
except:
    print("Database Connection Failed.")

# Flags and Declarations
keep_active_flag = True

# Regex Patterns
yes_no = '[YNyn]'
operation_pattern = '^(ADD|DEL|add|del|SHOW|show)$'
name_pattern = r"^[A-Z]{1}([a-zA-Z]{0,2}|['A-Z]{2})[a-z]{1,20}, [A-Z]{1}[a-z]{1,20}[\-\s]{0,1}[A-Z]{0,1}[a-z]{1,20}$"
phone_pattern = r"[+]\d{1,2} \d{3}-\d{3}-\d{4}"

# Create Table Query
create_cd_table = """
CREATE TABLE CDirectory (
ContactName VARCHAR(100),
PhoneNumber VARCHAR(20)
);
"""

# Show All Records Query
show_all_records = "SELECT * FROM CDirectory;"

# Create Table
try:
    cursor.execute(create_cd_table)
    print("Using the Contact Directory Database")
except:
    print("Using the Contact Directory Database")

# Active Application Session
while(keep_active_flag):

    # Add Another Record
    add_another_flag = input("Continue to Console Contact Directory? (Y/N) ")

    # Repeat Operation Loop
    if (re.match(yes_no, add_another_flag) and add_another_flag != None):
        if (add_another_flag.lower() == 'y'):
            operation = input("Add or Delete record? (ADD/DEL/SHOW) ")
            
            # Add or Delete Loop
            if(re.match(operation_pattern, operation) and operation != None):
                
                # Add Record
                if(operation.lower() == 'add'):
                    
                    # Input Record Name
                    contact_name = input("Enter a name: ")
                    
                    # Name Pattern Matching
                    name_match_flag = re.match(name_pattern, contact_name)
                    if (name_match_flag == None):
                        print("Invalid Name Format (Required: <xxxx>, <xxxx>)")
                        continue
                    print(contact_name)

                    # Input Record Phone Number
                    phone_number = input("Enter the phone number: ")

                    # Phone Number Pattern Matching
                    phone_number_match_flag = re.match(phone_pattern, phone_number)
                    if (phone_number_match_flag == None):
                        print("Invalid Phone Number Format (Required: +dd ddd-ddd-dddd)")
                        continue                    

                    # DB Insert Operation Execution
                    try:
                        cursor.execute("INSERT INTO CDirectory VALUES (?, ?)", (contact_name, phone_number))                        
                    except:
                        print("No Database.")
                
                # Delete Record
                elif(operation.lower() == 'del'):
                    to_delete = input("Enter name or phone number to delete contact: ")
                    if(re.match(name_pattern, to_delete) == None and re.match(phone_pattern,to_delete) == None):
                        print("Invalid Input")
                        continue
                    elif(re.match(name_pattern, to_delete) != None):
                        try:
                            cursor.execute("DELETE FROM CDirectory WHERE ContactName=(?)", (to_delete,)) 
                            print("Contact Deleted.")
                        except:
                            print("No Database.")
                            continue
                    elif(re.match(phone_pattern, to_delete) != None):
                        try:
                            cursor.execute("DELETE FROM CDirectory WHERE PhoneNumber=(?)", (to_delete,)) 
                            print("Contact Deleted.")
                        except:
                            print("No Database.")
                            continue
                
                # Display All Records
                elif(operation.lower() == 'show'):
                    try:
                        cursor.execute(show_all_records)
                        full_list = cursor.fetchall()
                        if (len(full_list) == 0):
                            print("No Records")
                        else:
                            print("All Records:")
                            for item in full_list:
                                print(item)
                    except:
                        print("No Database.")
            
            # Default Loop Back
            else:
                print("No such operation.")
        
        # Exit Application
        elif (add_another_flag.lower() == 'n'):
            print("Thank you for choosing to use this application.")
            break
    
    # Default Loop Back
    else:
        print("Invalid Entry.")

# Commit To DB
connection.commit()

# Close DB Connection
connection.close()
