#Database Management System for Bank
import mysql.connector as sql

mydb = sql.connect(
    host="localhost",
    user="root",
    passwd="Italy@2030",
    database="bank"
)

cursor = mydb.cursor()

def db_query(str):
    cursor.execute(str)
    result = cursor.fetchall()
    return result

def createcustomertable():
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers
               (username VARChAR(20) NOT NULL,
               password VARCHAR(20) NOT NULL,
               name VARCHAR(20) NOT NULL,
               age INTEGER NOT NULL,
               city VARCHAR(20) NOT NULL,
               balance INTEGER NOT NULL,
               account_number INTEGER NOT NULL,
               status BOOLEAN NOT NULL)
    ''')

mydb.commit()

if __name__ == "__main__":
    createcustomertable()