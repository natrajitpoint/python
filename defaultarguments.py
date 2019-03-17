def student(sno, sname, cls, m1,m2,m3,m4,m5,m6=0):
    tot = 0
    avg = 0
    if cls == '10thClass':
        tot = m1+m2+m3+m4+m5+m6
        avg = tot/6
    else:
        tot = m1+m2+m3+m4+m5
        avg = tot/5
    print("RollNo : {}\nName : {}\nClass : {}\nTotal : {}\
\nAverage : {}\n".format(sno,sname,cls,tot,avg))

#main
student(101, 'Ravi','Inter',70,70,70,70,70)
student(102, 'Kumar','10thClass',72,98,95,79,88, 66)

