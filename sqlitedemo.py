import sqlite3

demo=(sqlite3.connect("sqlite.db"))

demo.execute('''
Create table student (
  st_id INT AUTO_INCREMENT PRIMARY KEY,
  st_name VARCHAR(50),
  st_Class VARCHAR(10),
  st_Email VARCHAR(30)
)




''')

demo.close()