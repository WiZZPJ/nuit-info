from mysql.connector import connect
import os


def conn():
    cnx = connect(user="nuitinfo", password=os.environ['DB_PASS'], host="192.46.233.100", database="nuitinfo")
    c = cnx.cursor()
    return cnx, c

def query(c, request, param=None):
    c.execute(request, param)
    return c.fetchall()

def query_one(c, request, param=None):
    c.execute(request, param)
    return c.fetchone()