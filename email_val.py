
from email_validator import validate_email
from pandas import DataFrame, read_csv
import pandas as pd

import validate_email
import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='django-emails',
                                         user='root',
                                         password='root')
    sql_select_Query = "SELECT * FROM `django-emails`.emails_document"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    print("Total number of rows in table: ", cursor.rowcount)

    print("\nPrinting each row")
    for row in records:
        print("Id = ", row[0], )
        print("descritption = ", row[1])
        print("document  = ", row[2])
        print("uploaded_at  = ", row[3], "\n")
        print("user_id  = ", row[4], "\n")

except mysql.connector.Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if connection.is_connected():
        connection.close()


def validate(doc):
    file =r'doc'
    df=pd.read_csv(file,usecols =['email'])
    print(df)