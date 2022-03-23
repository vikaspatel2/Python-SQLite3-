import sqlite3

demo=(sqlite3.connect("sqlite.db"))

insert ='''
insert into student(st_id,st_name,sd_Class,sd_Email) VALUES
("2","KAJAL","12th"," kajal@gmal.com")

'''
demo.execute(insert)
demo.commit()
demo.close()