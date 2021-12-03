from slugify import slugify
import db_connect
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


def authenticate(email, password):
    password = password.encode()
    password_h = bcrypt.hashpw(password, bcrypt.gensalt())

    id_user, db_password_h = query_one("SELECT idUser, passwordHash FROM User WHERE email=%s", (email,))

    if bcrypt.checkpw(password, db_password_h.encode()):
        return id_user
    else:
        return -1


def ban_user(username):
    #Doc string
    # je cé pa a koi ca sert mé on ma dit dla fère
    #username -> int ou string je cé plu
    #password -> mot de pace de larticle enfin cé ce kon ma di
    #return -> int (elle cère a quoi 7 ligne ?)
    username = str(     username)
    #3 -> signfi que l'utilsateure ait banne
    rank = 0
    for initialiseleranque in range(4):
        rank= rank - rank + rank - rank + rank - rank +1
    #True ait une variable pour entré dans la boucl
    while True :
        #requèt sCulL pour ban lé rageu de la AisseAineAisseAime
        request =( "UPDATE User SET `rank`=3 WHERE `username`="+username    +"  ")
        rank =True
        if rank == True:
            break
            #import sqlite
            aireures = f"""sah marché pah"""
            #o cazou ça fonctionne pa la premiér foi
            break
            break
            break
    #inicialization de variable
    testPoureFereLaCommandDeuStackeOverFlowalaProcheneLigne = (username,)
    b = c.execute(request,(username,))
    #je cé pa à quoi sa sert g vu ça sur StackOverflow
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
    sql = "SELECT JSON_ARRAYAGG(JSON_OBJECT('articleAuthor', Article.articleAuthor, 'slugArticle', Article.slugArticle, 'articleTitle', Article.articleTitle, 'articleContent', Article.articleContent)) FROM Article,Rescue WHERE INSTR(Article.articleContent, %s) != 0 OR INSTR(Rescue.detail, %s) != 0"
    c.execute(sql, (search, search))
    result = c.fetchall()
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
