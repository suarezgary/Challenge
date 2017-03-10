import sqlite3
import Data.GetCategoriesReq as GetCategoriesReq
import Data.CategoriesSQLite
import utils.CategoriesMapper

#GetCategories = GetCategoriesReq.GetCategoriesRequest()
#CategoryList = GetCategories.GetCategoriesObjectFromText()

CategoriesDB = Data.CategoriesSQLite.Categories()
#try:
#    CategoriesDB.createTable()
#except:
#    print("BDD ya existente, eliminaremos la data y pasamos a agregar nueva...")
#    CategoriesDB.deleteTable()
#    CategoriesDB.createTable()

#CategoriesDB.insertList(CategoryList)

mapper = utils.CategoriesMapper.Mapper()

object = mapper.newObject()