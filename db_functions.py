from slugify import slugify

import mysql.connector
import db_connect
import json as json
import uuid

cnx, c = db_connect.conn()

"""
" Utilities
"""

def query(request, param=None):
    c.execute(request, param)
    return c.fetchall()

def query_one(request, param=None):
    c.execute(request, param)
    return c.fetchone()


def generate_token():
    return uuid.uuid4().hex


"""
" User
"""

def get_iduser_by_username(username):
    return query_one("SELECT idUser FROM User WHERE username=%s", (username,))[0]

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

    password_h = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    token = generate_token()

    c.execute("INSERT INTO User(username, passwordHash, userEmail, token) VALUES (%s, %s, %s, %s)", (username, password_h, email, token))
    cnx.commit()

    return token


def authenticate(username, password):
    password = password.encode()
    password_h = bcrypt.hashpw(password, bcrypt.gensalt())

    id_user, db_password_h = query_one("SELECT idUser, passwordHash FROM User WHERE username=%s", (username,))

    if bcrypt.checkpw(password, db_password_h.encode()):
        return id_user
    else:
        return -1


def ban_user(username):
    request = ("UPDATE User SET `rank`=3 WHERE `username`=%s")
    c.execute(request,(username,))
    cnx.commit()


def is_banned(id_user):
    return BANNED == query_one("SELECT `rank` FROM User WHERE idUser=%s", (id_user,))[0]


"""
" Article
"""

def add_article(title, content, user):
    slug = slugify(title)
    sql = "INSERT INTO Article (slugArticle, articleTitle, articleContent, accepted, active, articleAuthor) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (slug, title, content, False, False, user)

    c.execute(sql, val)
    cnx.commit()

    print (c.rowcount, "record inserted.")


def recherche_article(search):
    sql = "SELECT * FROM Article,Rescue WHERE INSTR(Article.articleContent, %s) != 0 OR INSTR(Rescue.detail, %s) != 0"
    cursor.execute(sql, (search, search))
    result = cursor.fetchall()
    return result


"""
" Rescue
"""

def add_rescue(rescueDate, peopleSaved, detail, source, crew, accepted, active, boatUsed, rescueAuthor):
    request = ("INSERT INTO Rescue (rescueDate,peopleSaved,detail,source,crew,accepted,active,boatUsed,rescueAuthor) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    c.execute(request, (rescueDate, peopleSaved, detail, source, crew, accepted, active, boatUsed, rescueAuthor))
    cnx.commit()


def update_rescue(idRescue,attribut,data):
    request = ("UPDATE User SET `%s`= %s WHERE `idRescue`=%s")
    c.execute(request,(attribut,data,idRescue))
    cnx.commit()


"""
" Boat
"""

def get_idboat_by_nomboat(nomboat):
    return db_connect.query_one(c, "SELECT idBoat FROM Boat WHERE nomBoat=%s", (nomboat,))[0]


cnx.close()
