students = ['Srinivasulu', 'Ravi', 'Nataraj','Bharadwaj']

for sname in students:
    v = ""
    c = 0
    for ch in sname:
        if ch in ['a','e','i','o','u','A','E','I','O','U']:
            v += ch + " "
            c += 1
    else:
        print("Vowels in %s : %s" %(sname,v))
        print("No of vowels in %s : %d\n" %(sname,c))
        

