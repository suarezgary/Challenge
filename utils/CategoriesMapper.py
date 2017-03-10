import Data.CategoriesSQLite 
import json

CategoriesDB = Data.CategoriesSQLite.Categories()

class Category:
    def __init__(self, id, level, name, parent_id):
        self.id = id
        self.level = level
        self.name = name
        self.parent_id = parent_id
        self.childs = []

    def appedChild(self, child):
        self.childs.append(child)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

class Mapper:
    def __init__(self):
        self.name = 'Gary'

    #No funciona creando el objeto de Arbol ya que consume mucha memoria
    def newObject(self):
        CategoriesObject = []
        test = CategoriesDB.getLevel(1).fetchall()
        print(test)
        for cat in test:
            newcategory = Category(cat[0], cat[1], cat[2], cat[3])
            CategoriesObject.append(newcategory)

            for firstLevel in CategoriesObject:
                self.appendChilds(firstLevel)
                for secondLevel in firstLevel.childs:
                    self.appendChilds(secondLevel)
                    for thirdLevel in secondLevel.childs:
                        self.appendChilds(secondLevel)

        print(CategoriesObject[0].childs[1].childs[2].childs[3].name)
        return CategoriesObject

    def appendChilds(self, parent):
        Childs = CategoriesDB.getChilds(parent.id).fetchall()
        for child in Childs:
            newcategory = Category(child[0], child[1], child[2], child[3])
            parent.appedChild(newcategory)