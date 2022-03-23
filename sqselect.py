import sqlite3

demo=sqlite3.connect("sqlite.db")

main=demo.execute("SELECT * FROM student limit 2,2")
print("STUDENT ID","STUDENT NAME","STUDENT STD","STUDENT EMAIL")
    
for x in main:
    print(x[0],"      " ,x[1],"      ", x[2],"      " ,x[3])