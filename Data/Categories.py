import sqlite3


class Categories:
    def __init__(self, db_name="Categories.db"):
        self.dbname = db_name

    def createTable(self):
        conn = sqlite3.connect(self.dbname)

        c = conn.cursor()

        # Create table
        c.execute('''CREATE TABLE categories
                    (ID INTEGER, level INTEGER, name text, parent_id INTEGER)''')

        # Save (commit) the changes
        conn.commit()

        # We can also close the connection if we are done with it.
        # Just be sure any changes have been committed or they will be lost.
        conn.close()

    def insert(self, Id, Level, Name, ParentId):
        conn = sqlite3.connect(self.dbname)

        c = conn.cursor()

        # Insert a row of data
        c.execute("INSERT INTO categories VALUES (" + Id + ", " + Level +", 'HJola ME llamo Gary', 1)")

        # Save (commit) the changes
        conn.commit()

        # We can also close the connection if we are done with it.
        # Just be sure any changes have been committed or they will be lost.
        conn.close()

    def insertList(self, CategoryList):
        conn = sqlite3.connect(self.dbname)

        c = conn.cursor()

        # Insert a row of data
        c.executemany("INSERT INTO categories VALUES (?,?,?,?)", CategoryList)

        # Save (commit) the changes
        conn.commit()

        # We can also close the connection if we are done with it.
        # Just be sure any changes have been committed or they will be lost.
        conn.close()

    def deleteTable(self):
        conn = sqlite3.connect(self.dbname)

        c = conn.cursor()

        # Create table
        c.execute('''DROP TABLE categories''')

        # Save (commit) the changes
        conn.commit()

        # We can also close the connection if we are done with it.
        # Just be sure any changes have been committed or they will be lost.
        conn.close()