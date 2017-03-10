import sqlite3


class Categories:
    def __init__(self, db_name="Categories.db"):
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()
        self.dbname = db_name

    def createTable(self):
        # Create table
        c.execute('''CREATE TABLE categories
                    (ID INTEGER, level INTEGER, name text, parent_id INTEGER)''')

        conn.commit()

    def insert(self, Id, Level, Name, ParentId):
        # Insert a row of data
        self.c.execute("INSERT INTO categories VALUES (" + Id + ", " + Level +", 'HJola ME llamo Gary', 1)")

        # Save (commit) the changes
        self.conn.commit()

    def insertList(self, CategoryList):
        c.executemany("INSERT INTO categories VALUES (?,?,?,?)", CategoryList)
        # Save (commit) the changes
        self.conn.commit()

    def getAll(self):
        rows = self.c.execute("SELECT * FROM categories")
        return rows

    def getChilds(self, parent_id):
        parameters = (parent_id, )

        rows = self.c.execute('SELECT * FROM categories WHERE parent_id=?', parameters)
        return rows

    def getLevel(self, level):
        parameters = (level, )

        rows = self.c.execute('SELECT * FROM categories WHERE level=?', parameters)
        return rows

    def deleteTable(self):
        # Create table
        self.c.execute('''DROP TABLE categories''')

        # Save (commit) the changes
        self.conn.commit()

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()