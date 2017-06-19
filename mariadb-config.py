#!/usr/bin/python
import mysql.connector as mariadb


def tableprint(tablename):
    if tablename in (table_list):
        cursor.execute("""select * from %s""" % (tablename))
        data = cursor.fetchall()
        for row in data:
            print(row)
    else:
        print("{} is not a valid table".format(tablename))

def rowprint(columnname):
    cursor.execute(""" select * from projects where id=%s""" % (columnname))
    data = cursor.fetchall()
    for row in data:
        print(row)

mariadb_connection = mariadb.connect(host='10.20.0.6', port='3306', user='thecasual', password='waterfall', database='python')
cursor = mariadb_connection.cursor()

cursor.execute("""show tables;""")
table_list = cursor.fetchall()

#databasemod = input("id,name,begin_date or end_date?")
databasemod="projects"
tableprint(databasemod)
#rowprint(databasemod)


