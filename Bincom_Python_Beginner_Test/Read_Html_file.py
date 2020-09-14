import codecs
import re
import psycopg2

# use relative path

file = codecs.open(r"Bincom Python Beginner Test\python_class_test.html", "r")
# print(file.read())

# find number of occurences of each color

txt = file.read()
red_count = len(re.findall("RED", txt))
yellow_count = len(re.findall("YELLOW", txt))
blue_count = len(re.findall("BLUE", txt))
pink_count = len(re.findall("PINK", txt))
green_count = len(re.findall("GREEN", txt))
brown_count = len(re.findall("BROWN", txt))
white_count = len(re.findall("WHITE", txt))

cream_count = len(re.findall("CREAM", txt))
orange_count = len(re.findall("ORANGE", txt))
arsh_count = len(re.findall("ARSH", txt))

# append color count to list

colors = {
    "Green": green_count,
    "Yellow": yellow_count,
    "Brown": brown_count,
    "Blue": blue_count,
    "Pink": pink_count,
    "Orange": orange_count,
    "Cream": cream_count,
    "Red": red_count,
    "White": white_count,
    "Arsh": arsh_count,
}

var_list = []
var_sum = 0
fibo = []


def mostWornColor():
    max_key = max(colors, key=colors.get)
    print("Most worn Color is ", max_key)


mostWornColor()


def mean():
    # number of occurences / total
    Mean = sum(colors.values()) / len(colors)
    print("Mean is: ", sum(colors.values()) / len(colors))


mean()


def variance():

    Mean = sum(colors.values()) / len(colors)
    for i in colors.values():
        var_list.append(i)

    # print(var_list)
    var = sum((i - Mean) ** 2 for i in var_list) / len(var_list)
    print("variance is: ", var)
    # print(Mean)


variance()


def red_probability():
    prob = colors.get("Red") / sum(colors.values())
    print("Probability of red = ", prob)


red_probability()


for i in colors.values():
    var_list.append(i)


def median(var_list):
    sortedLst = sorted(var_list)
    lstLen = len(var_list)
    index = (lstLen - 1) // 2

    if lstLen % 2:
        print("Median is: ", sortedLst[index])
    else:
        print("Median is: ", (sortedLst[index] + sortedLst[index + 1]) / 2.0)


median(var_list)

print(colors)

from psycopg2 import connect


# Database name is Shirt_color
# Table name is also Shirt_color
# conn = connect('dbname = Shirt_color')


# cur = conn.cursor()

# for i in colors:
#     cur.execute('INSERT INTO Shirt_color VALUES 'colors)


conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="postgres",
    host="127.0.0.1",
    port="5432",
)

conn.autocommit = True

cur = conn.cursor()


sql = """CREATE DATABASE Shirt_color"""

cur.execute(sql)
print("Database created succesfully")
conn.close()


conn = psycopg2.connect(
    database="Shirt_color",
    user="postgres",
    password="postgres",
    host="127.0.0.1",
    port="5432",
)

conn.autocommit = True

cur = conn.cursor()


sql = """CREATE TABLE Shirt_color(
    id BIGSERIAL NOT NULL PRIMARY KEY
    color CHAR(20) NOT NULL
    frequency INT NOT NULL)"""

cur.execute(sql)
print("Table created succesfully")

conn.close()

conn = psycopg2.connect(
    database="Shirt_color",
    user="postgres",
    password="postgres",
    host="127.0.0.1",
    port="5432",
)

conn.autocommit = True

cur = conn.cursor()


for i in colors:
    # sql = '''INSERT INTO Shirt_color(color,frequency) VALUES(%s,%s)'''
    cur.execute("INSERT INTO sometable (col1, col2) VALUES (%s, %s)", (i, colors[i]))

conn.close()
