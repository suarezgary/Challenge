#!/usr/bin/env python3
import os
import fileinput
import shutil

dir_path = os.path.dirname(os.path.realpath(__file__))

def createFile(self):
    TemplateFile = self.dir_path + '\\..\\templates\\table1.html'
    NewFile = self.dir_path + '\\..\\generated.html'
    shutil.copyfile(TemplateFile, NewFile)

def addRows(self, CategoryList):
    textToSearch = '{{table_info}}'
    textToReplace = ''
    for category in CategoryList:
        textToReplace = textToReplace + '''\n <tr data-depth="0" class="collapse level0">
                                                <td><span class="toggle collapse"></span>Item 1</td>
                                                <td>123</td>
                                            </tr>'''
    with fileinput.FileInput(NewFile, inplace=True) as file:
        for line in file:
            print(line.replace(textToSearch, textToReplace), end='')