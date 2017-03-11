#!/usr/bin/env python3
import os
import fileinput
import shutil
import Data.CategoriesSQLite

class plintHtml:
    def __init__(self):
        self.dir_path = os.path.dirname(os.path.realpath(__file__))

    def createFile(self):
        TemplateFile = self.dir_path + '\\..\\templates\\table1.html'
        self.NewFile = self.dir_path + '\\..\\generated.html'
        shutil.copyfile(TemplateFile, self.NewFile)


    def addRow(self, Category):
        textToSearch = '{{table_info}}'
        textToReplace = ''
        nivel = int(Category[1]) - 1
        textToReplace = textToReplace + '''\n <tr data-depth="{{level}}" class="collapse level{{level}}">
                                                <td><span class="toggle collapse"></span>{{id}}</td>
                                                <td>{{name}}</td>
                                                <td>{{bestoffer}}</td>
                                            </tr>'''
        textToReplace = textToReplace.replace("{{level}}",str(nivel))
        textToReplace = textToReplace.replace("{{id}}",str(Category[0]))
        textToReplace = textToReplace.replace("{{name}}",str(Category[2]))
        textToReplace = textToReplace.replace("{{bestoffer}}",'Best Offer')
        textToReplace = textToReplace + '{{table_info}}'
        with fileinput.FileInput(self.NewFile, inplace=True) as file:
            for line in file:
                print(line.replace(textToSearch, textToReplace), end='')


    def addRows(self, CategoryList):
        textToSearch = '{{table_info}}'
        textToReplace = ''
        for category in CategoryList:
            nivel = int(category[1]) - 1
            textToReplace = textToReplace + '''\n <tr data-depth="{{level}}" class="collapse level{{level}}">
                                                    <td><span class="toggle collapse"></span>{{id}}</td>
                                                    <td>{{name}}</td>
                                                    <td>{{bestoffer}}</td>
                                                </tr>
                                                {{{{id}}}}'''
            textToReplace = textToReplace.replace("{{level}}",str(nivel))
            textToReplace = textToReplace.replace("{{id}}",str(category[0]))
            textToReplace = textToReplace.replace("{{name}}",str(category[2]))
            textToReplace = textToReplace.replace("{{bestoffer}}",'Best Offer')
        #textToReplace = textToReplace + '{{table_info}}'
        with fileinput.FileInput(self.NewFile, inplace=True) as file:
            for line in file:
                print(line.replace(textToSearch, textToReplace), end='')

    
    def rowsInfoToReplace(self, CategoryList):
        textToReplace = ''
        for category in CategoryList:
            nivel = int(category[1]) - 1
            textToReplace = textToReplace + '''\n <tr data-depth="{{level}}" class="collapse level{{level}}">
                                                    <td><span class="toggle collapse"></span>{{id}}</td>
                                                    <td>{{name}}</td>
                                                    <td>{{bestoffer}}</td>
                                                </tr>
                                                {{{{id}}}}'''
            textToReplace = textToReplace.replace("{{level}}",str(nivel))
            textToReplace = textToReplace.replace("{{id}}",str(category[0]))
            textToReplace = textToReplace.replace("{{name}}",str(category[2]))
            textToReplace = textToReplace.replace("{{bestoffer}}",'Best Offer')
        return textToReplace
    
    def searchReplaceForID(self):
        CategoryDB = Data.CategoriesSQLite.Categories()
        initSearch = '{{'
        finSearch = '}}'
        textToSearch = ''
        textToReplace = ''
        hayDatos = True
        while hayDatos:
            with fileinput.FileInput(self.NewFile, inplace=True) as file:
                conteo = 0
                for line in file:
                    idStartIndex = line.find("{{")
                    idFinishIndex = line.find("}}")
                    if(idStartIndex != -1 and idFinishIndex != -1):
                        conteo = conteo + 1
                        id = line[idStartIndex+2:idFinishIndex]
                        textToSearch = '{{' + id + '}}'
                        childList = CategoryDB.getChilds(id)
                        textToReplace = self.rowsInfoToReplace(childList)
                    print(line.replace(textToSearch, textToReplace), end='')
                if(conteo == 0):
                    hayDatos = False

    def finishModify(self):
        textToSearch = '{{table_info}}'
        textToReplace = ''
        with fileinput.FileInput(self.NewFile, inplace=True) as file:
            for line in file:
                print(line.replace(textToSearch, textToReplace), end='')