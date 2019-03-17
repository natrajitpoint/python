import pymysql

try:
    # Open database connection 
    conn = pymysql.connect(host="localhost",
                         user="root",
                         passwd="itpoint",
                         db="DB5to6")
     
    # Create a Cursor object to execute queries.
    cur = conn.cursor()
     
    # Insert records into Books table 
    insertquery = "Insert into books values(%s,%s,%s,%s)"

    #Accept multiple records from user
    records = []
    n = int(input("How many books you want to insert : "))
    for i in range(n):
        bid = int(input("Enter Book Id : "))
        bname = input("Enter Book Name : ")
        author = input("Enter Author Name : ")
        price = float(input("Enter Book Price : "))
        r = [bid,bname,author,price]
        records.append(r)

    # Execute Query
    ret = cur.executemany(insertquery, records)
    conn.commit()
    print("%s records inserted successfully...." %ret)
except Exception as ex:
    conn.rollback()
    print(ex)
finally:
    # disconnect from server
    conn.close()

