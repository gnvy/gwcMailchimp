import mysql.connector
from mysql.connector import Error
from rating import email_opens

# Database credentials and details
host_name = "localhost"
db_name = "mydatabase"
user_name = "root"
user_password = "Cancer_0716"

# Connect to the MySQL database
try:
    connection = mysql.connector.connect(
        host=host_name,
        database=db_name,
        user=user_name,
        password=user_password
    )
    
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version", db_Info)
        
        cursor = connection.cursor()
        
        # Update ratings for each email
        for email, opens in email_opens.items():
            update_query = """
                UPDATE members
                SET rating = rating + %s
                WHERE email = %s;
            """
            cursor.execute(update_query, (opens, email))

        connection.commit()
        print("Ratings updated successfully.")

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
