import pymysql

# Open database connection 
conn = pymysql.connect(host="localhost",
                     user="root",
                     passwd="itpoint",
                     db="DB5to6")
 
# Create a Cursor object to execute queries.
cur = conn.cursor()
 
# Insert records into Books table 
deletequery = 'Delete from Books where bid = %s'

#Accept Data from user
bid = int(input("Enter Book Id : "))

try:
    # Execute Query
    ret = cur.execute(deletequery, [bid])
    conn.commit()
    if ret == 0:
        print("Book id not found")
    else:
        print("%s record deleted successfully" %ret)
except Exception as ex:
    conn.rollback()
    print(ex)
finally:
    # disconnect from server
    conn.close()

