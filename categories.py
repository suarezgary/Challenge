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

ListaCategorias = CategoriesDB.getLevel(1)
printhtml = utils.printHTML.plintHtml()
printhtml.createFile()
printhtml.addRows(ListaCategorias)
printhtml.searchReplaceForID()
printhtml.finishModify()