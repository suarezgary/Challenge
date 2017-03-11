#!/usr/bin/env python3
import os
import fileinput
import shutil

class plintHtml:
    def __init__(self):
        self.dir_path = os.path.dirname(os.path.realpath(__file__))

    def createFile(self):
        TemplateFile = self.dir_path + '\\..\\templates\\table1.html'
        self.NewFile = self.dir_path + '\\..\\generated.html'
        shutil.copyfile(TemplateFile, self.NewFile)

    def addRows(self, CategoryList):
        textToSearch = '{{table_info}}'
        textToReplace = ''
        for category in CategoryList:
            nivel = int(category[1]) - 1
            textToReplace = textToReplace + '''\n <tr data-depth="{{level}}" class="collapse level{{level}}">
                                                    <td><span class="toggle collapse"></span>{{id}}</td>
                                                    <td>{{name}}</td>
                                                    <td>{{bestoffer}}</td>
                                                </tr>'''
            textToReplace = textToReplace.replace("{{level}}",str(nivel))
            textToReplace = textToReplace.replace("{{id}}",str(category[0]))
            textToReplace = textToReplace.replace("{{name}}",str(category[2]))
        textToReplace = textToReplace + '{{table_info}}'
        with fileinput.FileInput(self.NewFile, inplace=True) as file:
            for line in file:
                print(line.replace(textToSearch, textToReplace), end='')

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
        textToReplace = textToReplace + '{{table_info}}'
        with fileinput.FileInput(self.NewFile, inplace=True) as file:
            for line in file:
                print(line.replace(textToSearch, textToReplace), end='')
        
    def finishModify(self):
        textToSearch = '{{table_info}}'
        textToReplace = ''
        with fileinput.FileInput(self.NewFile, inplace=True) as file:
            for line in file:
                print(line.replace(textToSearch, textToReplace), end='')