import sqlite3

demo=sqlite3.connect("sqlite.db")

demo.execute('''
 
update student set st_id="1" where st_id=null

''')
demo.commit()
demo.close()