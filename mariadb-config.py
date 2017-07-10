#!/usr/bin/python
import mysql.connector as mariadb

mariadb_connection = mariadb.connect(host='10.20.0.7', port='3306', user='thecasual', password='!QAZ2wsx', database='project', autocommit=True, buffered=True)
cursor = mariadb_connection.cursor()

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def get_column_len(self):
        cursor.execute("""desc %s""" % (self))
        data = cursor.fetchall()
        length = 0
        for row in data:
            length += 1
        column_size=(length - 1)

    def tableprint(tablename):
        cursor.execute("""select * from %s""" % (tablename))
        data = cursor.fetchall()
        for row in data:
            print(row)

    def rowprint(columnname):
        cursor.execute(""" select * from projects where id=%s""" % (columnname))
        data = cursor.fetchall()
        for row in data:
            print(row)

    def add_employee(self):
        new_employee = """insert into employee ( first_name, last_name ) values (%s, %s)"""
        cursor.execute(new_employee, (self.first, self.last))

rach = Employee('Dan', 'Smith')


###Working on adding variable length column names to expand SQL statement
#print("""insert into employee ( """ + '%s, ' * int(column_size) + """ ) """)

#Employee.tableprint("employee")
cursor.close()


