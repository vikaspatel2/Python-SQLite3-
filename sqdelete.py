import sqlite3

demo=sqlite3.connect("sqlite.db")

st_id=input("Enter the student id: ")

demo.execute("DELETE FROM student where st_id ="+ st_id )

demo.commit()
demo.close()