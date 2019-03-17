import pymysql

try:
    # Open database connection 
    conn = pymysql.connect(host="localhost",
                         user="root",
                         password="itpoint",
                         db="DB5to6")
     
    # Create a Cursor object to execute queries.
    cur = conn.cursor()
     
    # Create Books table 
    query = """Create Table Books
        (
        bid int primary key,
        bname varchar(25) not null,
        author varchar(30) not null,
        price float not null
        );"""

    # Execute Query
    cur.execute(query)    
    print("Books table created successfully...")
except Exception as ex:
    print(ex)
finally:
    # disconnect from server
    conn.close()

