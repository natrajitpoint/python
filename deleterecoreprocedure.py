import pymysql
try:
    # Open database connection 
    conn = pymysql.connect(host="localhost",
                         user="root",
                         passwd="itpoint",
                         db="DB5to6")
     
    # Create a Cursor object to execute queries.
    cur = conn.cursor()

    #Accept student details from user
    sno = int(input("Enter Roll Number : "))
    
    ret = cur.callproc('DeleteStu',[sno])
    print("%s student details deleted...." %ret[0])
    conn.commit()
except Exception as ex:
    conn.rollback()
    print(ex)
finally:
    conn.close()
 

