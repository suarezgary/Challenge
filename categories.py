import sqlite3
import Data.GetCategoriesReq as GetCategoriesReq
import Data.CategoriesSQLite
import utils.CategoriesMapper
import utils.printHTML

def childPrint(category):
    printhtml.addRow(category)
    childList = CategoriesDB.getChilds(firstlevel[0], firstlevel[1])
    if(len(childList) > 0):
        for child in childList:
            #childPrint(child)
            printhtml.addRow(child)

GetCategories = GetCategoriesReq.GetCategoriesRequest()
CategoryList = GetCategories.GetCategoriesObjectFromText()

CategoriesDB = Data.CategoriesSQLite.Categories()
try:
    CategoriesDB.createTable()
except:
    print("BDD ya existente, eliminaremos la data y pasamos a agregar nueva...")
    CategoriesDB.deleteTable()
    CategoriesDB.createTable()

CategoriesDB.insertList(CategoryList)

#mapper = utils.CategoriesMapper.Mapper()
ListaCategorias = CategoriesDB.getLevel(1)
printhtml = utils.printHTML.plintHtml()
printhtml.createFile()
for firstlevel in ListaCategorias:
    childPrint(firstlevel)
    #printhtml.addRow(firstlevel)
    #childList = CategoriesDB.getChilds(firstlevel[0], firstlevel[1])
    #printhtml.addRows(childList)
printhtml.finishModify()
#object = mapper.newObject()