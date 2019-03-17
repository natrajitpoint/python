import pymysql

# Open database connection 
conn = pymysql.connect(host="localhost",
                     user="root",
                     passwd="itpoint",
                     db="DB5to6")
 
# Create a Cursor object to execute queries.
cur = conn.cursor()
 
# Insert records into Books table 
insertquery = "Insert into books values(%s,%s,%s,%s)"

#Accept Data from user
bid = int(input("Enter Book Id : "))
name = input("Enter Book Name : ")
author = input("Enter Author Name : ")
price = float(input("Enter Book Price : "))

try:
    # Execute Query
    ret = cur.execute(insertquery, [bid, name, author,price])
    conn.commit()
    print("%s rows inserted successfully...." %ret)
except Exception as ex:
    conn.rollback()
    print(ex)
finally:
    # disconnect from server
    conn.close()

