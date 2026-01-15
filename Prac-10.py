import mysql.connector 
 
# Connect to MySQL database 
conn = mysql.connector.connect( 
    host='localhost',          
    user='root',      
    password='Reki2005#',  
    database='rekidb'   
) 
 
cursor = conn.cursor() 
 
# Create table  
query = """CREATE TABLE IF NOT EXISTS class( 
              Name VARCHAR(100), 
              Marks FLOAT, 
              Subject VARCHAR(100) 
           )""" 
cursor.execute(query) 
print("Table created successfully") 
 
# Insert multiple data 
n = int(input("Enter number of students: ")) 
 
for i in range(n): 
    query2 = "INSERT INTO class (Name, Marks, Subject) VALUES (%s, %s, %s)" 
    name = input(f"Enter name of student {i+1}: ") 
    marks = float(input("Enter marks: ")) 
    subject = input("Enter subject: ") 
 
    cursor.execute(query2, (name, marks, subject)) 
    conn.commit() 
    print(f"Student {i+1} inserted successfully!") 

# Select query 
query3 = "SELECT * FROM class WHERE Marks >= 80" 
cursor.execute(query3) 
results = cursor.fetchall() 
print("\nStudents with Marks >= 80:") 
for row in results: 
    print(row) 

# Delete query 
n = input("ENTER NAME OF THE STUDENT TO BE DELETED : ") 
query4 = "DELETE FROM class WHERE Name = %s"  
cursor.execute(query4, (n,))
conn.commit()
print(n,"deleted sucessfully") 
# Close the connection 
conn.close()