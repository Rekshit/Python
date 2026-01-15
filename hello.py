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

# Delete query 
n = input("ENTER NAME OF THE STUDENT TO BE DELETED : ") 
query4 = "DELETE FROM class WHERE Name = %s"  
cursor.execute(query4, (n,))
conn.commit()
print(n,"deleted sucessfully") 
# Close the connection 
conn.close()