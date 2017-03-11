import sqlite3
import Data.GetCategoriesReq as GetCategoriesReq
import Data.CategoriesSQLite
import utils.CategoriesMapper
import utils.printHTML


GetCategories = GetCategoriesReq.GetCategoriesRequest()
CategoriesDB = Data.CategoriesSQLite.Categories()
printhtml = utils.printHTML.plintHtml()

def PopulateBDD():
    CategoryList = GetCategories.GetCategoriesObject()
    try:
        CategoriesDB.createTable()
    except:
        print("BDD ya existente, eliminaremos la data y pasamos a agregar nueva...")
        CategoriesDB.deleteTable()
        CategoriesDB.createTable()
    CategoriesDB.insertList(CategoryList)

def GenerateAll():
    ListaCategorias = CategoriesDB.getLevel(1)
    print('Generating html File')
    printhtml.createFile()
    printhtml.addRows(ListaCategorias)
    printhtml.searchReplaceForID()
    printhtml.finishModify()

def GenerateByID(id):
    ListaCategorias = CategoriesDB.getByID(id)
    if(len(ListaCategorias) == 0):
        print('No category with ID: ' + str(id))
    else:
        print(len(ListaCategorias))
        print('Generating html File')
        printhtml.createFile()
        printhtml.addRows(ListaCategorias)
        printhtml.searchReplaceForID()
        printhtml.finishModify()

#PopulateBDD()
GenerateAll()
#GenerateByID(872)