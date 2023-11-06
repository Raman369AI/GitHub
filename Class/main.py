import pandas as pd
import csv
from mysql.connector import connection
from urllib3.filepost import writer

# create a mySQL connection
cnx = connection.MySQLConnection(user='readonlyuser',password='Msis5193Fall2023',host='34.70.89.75',database='Northwind')
cursor = cnx.cursor()
cursor.execute("select * from Product")
with open("out.csv", "w", newline='') as csv_file:  # Python 3 version
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([i[0] for i in cursor.description])
    for y in cursor:
        print(list(y))
        csv_writer.writerow(list(y))

cursor1 = cnx.cursor()
cursor1.execute("select * from Category")
with open("out2.csv", "w", newline='') as csv_file:  # Python 3 version
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([i[0] for i in cursor1.description])
    for x in cursor1:
        print(list(x))
        csv_writer.writerow(list(x))

product=pd.read_csv('out.csv')

category=pd.read_csv('out2.csv')
left_join=pd.merge(product,category,on='categoryId',how='outer')
true=left_join.groupby(['categoryName']).agg({'productId':'count'})
print(true)
true.to_csv('out3.csv')




