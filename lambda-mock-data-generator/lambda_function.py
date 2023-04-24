import pymysql
import os

# Set the connection parameters
rds_host = os.environ['RDS_HOST']
name = os.environ['DB_NAME']
password = os.environ['DB_PASSWORD']
user = os.environ['DB_USER']

def lambda_handler(event, context):
    print("updated")
    try:
        # Connect to the database
        conn = pymysql.connect(rds_host, user=user, passwd=password, db=name, connect_timeout=5)

        # # Create a table
        # with conn.cursor() as cur:
        #     cur.execute("CREATE TABLE Employees (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(255) NOT NULL, PRIMARY KEY (id))")

        # # Insert sample data
        # with conn.cursor() as cur:
        #     cur.execute("INSERT INTO Employees (name) VALUES ('John'), ('Jane'), ('Bob')")
        #     conn.commit()

    except pymysql.MySQLError as e:
        print("Error connecting to MySQL: ", e)
        raise Exception("Unable to connect to the database")
    except Exception as e:
        print("Error: ", e)
        raise Exception("An error occurred while executing the function")
    finally:
        # Close the database connection
        conn.close()
