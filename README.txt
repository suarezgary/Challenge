This project was created by Gary Suarez.

It handles a request to the "GetCategories" service of the Ebay API, then proccess the data into a SQLite DB.
Also, it can print the categories into a html file with a Table tree.

-To make the request and populate the database (categories.db file) you can make the following command:
./categories.py -b or ./categories.py --rebuild

-To make a html with all the categories Table:
./categories.py -a  or ./categories.py --renderall

-To make a html of one specific ID and it's childs:
./categories.py -r <id>  or ./categories.py -r <id>   (ex. ./categories.py -r 872)

Note: I also created a class that can read xml file with the same API information,
if you want to save time with testing (like me), change the code to use that working method instead.