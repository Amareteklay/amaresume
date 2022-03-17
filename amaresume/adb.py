import psycopg2

#connect to the db 
con = psycopg2.connect(
            host = "localhost",
            database="amandb",
            user = "gitpod",
            password = "")

#cursor 
cur = con.cursor()

cur.execute("insert into students (id, name) values (%s, %s)", (1, "Aman") )

#execute query
cur.execute("select id, name from students")

rows = cur.fetchall()

for r in rows:
    print (f"id {r[0]} name {r[1]}")

#commit the transcation 
con.commit()

#close the cursor
cur.close()

#close the connection
con.close()