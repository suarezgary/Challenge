import sqlite3


class Categories:
    def __init__(self, db_name="Categories.db"):
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()
        self.dbname = db_name

    def createTable(self):
        # Create table
        self.c.execute('''CREATE TABLE categories
                    (ID INTEGER, level INTEGER, name text, parent_id INTEGER)''')

        self.conn.commit()

    def insert(self, Id, Level, Name, ParentId):
        # Insert a row of data
        self.c.execute("INSERT INTO categories VALUES (" + Id + ", " + Level +", 'HJola ME llamo Gary', 1)")

        # Save (commit) the changes
        self.conn.commit()

    def insertList(self, CategoryList):
        self.c.executemany("INSERT INTO categories VALUES (?,?,?,?)", CategoryList)
        # Save (commit) the changes
        self.conn.commit()

    def getAll(self):
        rows = self.c.execute("SELECT * FROM categories")
        return rows.fetchall()

    def getByID(self, id):
        parameters = (id, )
        rows = self.c.execute('SELECT * FROM categories WHERE id=?', parameters)
        return rows.fetchall()

    def getChilds(self, parent_id, parent_level = -1):
        if(parent_level == -1):
            parent = self.getByID(parent_id)
            parent_level = parent[0][1]
        childLevel = int(parent_level) + 1
        parameters = (parent_id, childLevel)

        rows = self.c.execute('SELECT * FROM categories WHERE parent_id=? AND level=?', parameters)
        return rows.fetchall()

    def getLevel(self, level):
        parameters = (level, )

        rows = self.c.execute('SELECT * FROM categories WHERE level=?', parameters)
        return rows.fetchall()

    def deleteTable(self):
        # Create table
        self.c.execute('''DROP TABLE categories''')

        # Save (commit) the changes
        self.conn.commit()

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()