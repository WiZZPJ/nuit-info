import mysql.connector
import db_connect
from slugify import slugify
import json as json
import uuid
cnx,c = db_connect.conn()

def query(request, param=None):
    c.execute(request, param)
    return c.fetchall()

def query_one(request, param=None):
    c.execute(request, param)
    return c.fetchone()


def generate_token():
    return uuid.uuid4().hex


def get_iduser_by_username(username):
    return query_one("SELECT idUser FROM User WHERE username=%s", (username,))[0]


def register_user(username, password, email):
    if 1 <= query_one("SELECT COUNT(idUser) FROM User WHERE username=%s", (username,))[0]:
        print("A user with this username already exists.")
        return -1

    if 1 <= query_one("SELECT COUNT(idUser) FROM User WHERE userEmail=%s", (email,))[0]:
        print("A user with this email already exists.")
        return -1

    password_h = bcrypt.hashpw(password, bcrypt.gensalt())
    token = generate_token()

    c.execute("INSERT INTO User(username, passwordHash, userEmail, token) VALUES (%s, %s, %s, %s)", (username, password_h, email, token))
    cnx.commit()

def add_article(title, content, user):
    c = cnx.cursor
    slug = slugify(title)
    sql = "INSERT INTO Article (slugArticle, articleTitle, articleContent, accepted, active, articleAuthor) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (slug, title, content, False, False, user)

    c.execute(sql, val)
    cnx.commit()
    c.close()
    print (c.rowcount, "record inserted.")



def ban_user(username):
    c = cnx.cursor()
    request = ("UPDATE User SET `rank`=3 WHERE `username`=%s")
    c.execute(request,(username,))
    cnx.commit()
    c.close()


def add_rescue(rescueDate,peopleSaved,detail,source,crew,accepted,active,boatUsed,rescueAuthor):
    c = cnx.cursor()
    request = ("INSERT INTO Rescue (rescueDate,peopleSaved,detail,source,crew,accepted,active,boatUsed,rescueAuthor) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    c.execute(request,(rescueDate,peopleSaved,detail,source,crew,accepted,active,boatUsed,rescueAuthor))
    cnx.commit()
    c.close()




def update_rescue(idRescue,attribut,data):
    request = ("UPDATE User SET `%s`= %s WHERE `idRescue`=%s")
    c.execute(request,(attribut,data,idRescue))
    cnx.commit()
    c.close()
    
def get_idboat_by_nomboat(nomboat):
    return db_connect.query_one(c, "SELECT idBoat FROM Boat WHERE nomBoat=%s", (nomboat,))[0]


cnx.close()




