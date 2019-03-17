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
    name = input("Enter Student Name : ")
    cls = input("Enter Student Class : ")
    s1 = int(input("Enter first subject marks : "))
    s2 = int(input("Enter second subject marks : "))
    s3 = int(input("Enter third subject marks : "))

    ret = cur.callproc('InsertStu',[sno,name,cls,s1,s2,s3])
    print("%s student details inserted...." %ret[0])
    conn.commit()
except Exception as ex:
    conn.rollback()
    print(ex)
finally:
    conn.close()
 

