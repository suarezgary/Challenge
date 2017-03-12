#!/usr/bin/python
#Created By Gary Suarez 10/03/2017
import sys, getopt
import sqlite3
import Data.GetCategoriesReq as GetCategoriesReq
import Data.CategoriesSQLite
import utils.printHTML


GetCategories = GetCategoriesReq.GetCategoriesRequest()
CategoriesDB = Data.CategoriesSQLite.Categories()
printhtml = utils.printHTML.plintHtml()

def PopulateBDD():
    print('Fetching data from api, please wait this can take some time...')
    CategoryList = GetCategories.GetCategoriesObject()
    print('Creating Table...')
    try:
        CategoriesDB.createTable()
    except:
        print('Droping table and recreating...')
        CategoriesDB.deleteTable()
        CategoriesDB.createTable()
    CategoriesDB.insertList(CategoryList)

def GenerateAll():
    ListaCategorias = CategoriesDB.getLevel(1)
    print('Generating html File, please wait this can take some time...')
    printhtml.createFile()
    printhtml.addRows(ListaCategorias)
    printhtml.searchReplaceForID()
    printhtml.finishModify()
    print('File Generated')

def GenerateByID(id):
    ListaCategorias = CategoriesDB.getByID(id)
    if(len(ListaCategorias) == 0):
        print('No category with ID: ' + str(id))
    else:
        print('Generating html File')
        printhtml.createFile(id)
        printhtml.addRows(ListaCategorias)
        printhtml.searchReplaceForID()
        printhtml.finishModify()
        print('File Generated')

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hr:ba",["rebuild","render=","renderall"])
    except getopt.GetoptError:
        print('categories.py -h to se the options')
        print('Press a button to continue...')
        input()
    if(len(opts) == 0):
        print('categories.py -h to se the options')
    else:
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                print ('categories.py -b -r <outputfile>\n Rebuild: -b or --rebuild\n Render: -r <categoryid> or --render <categoryid>.\n Render All: -a or --renderall')
                print('Press a button to continue...')
                input()
                sys.exit()
            elif opt in ("-r", "--render"):
                category_id = arg
                GenerateByID(category_id)
            elif opt in ("-a", "--renderall"):
                GenerateAll()
            elif opt in ("-b", "--rebuild"):
                PopulateBDD()
    print('Press a button to continue...')
    input()

if __name__ == "__main__":
   main(sys.argv[1:])