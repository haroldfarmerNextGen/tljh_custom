import sqlite3
import grp
import os
import sys
from sqlite3 import Error
from pathlib import Path

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    
    return conn

def getUserID(conn,name):
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE name = '%s'" % name)
    result = cur.fetchall()
    return [x[0] for x in result]

def checkGroup(id, conn):
    cur = conn.cursor()
    cur.execute("SELECT group_id FROM user_group_map WHERE user_id = %s" % id)
    result = cur.fetchall()
    return [x[0] for x in result]

def setPermissions(grpID,name):
    if grpID == 1:
       print("Adding user to group")
       try:
           os.system("usermod -aG devs %s" % name)
           os.system("groups %s" % name)
       except(e):
           print(e.message())
    else:
       print("User Not Dev or Admin")

def checkUserExist(name):
    check = os.system("getent passwd jupyter-%s" % name)
    print("This is ",check)
    if check !=0 :
       return False
    else:
       return True

def addUser(conn,nam):
    try:
       con = conn.cursor()
       con.execute("INSERT INTO users (id,name) VALUES (15,'tod')")
    except Error as e:
       print(e)

def main():
    #TODO add user if not exist
    name = sys.argv[1]
    check = checkUserExist(name)
    if check == True:
        database = "jupyterhub.sqlite"
        # create a database connection
        conn = create_connection(database)
        userID =getUserID(conn,name)
        userID = userID[0]
        groupID = checkGroup(userID,conn)
        groupID = groupID[0]
        name = 'jupyter-' + name
        print("THis is name "+name) 
        setPermissions(groupID,name)
       
    else: 
        print("Here")
        name = 'test5'
        database = "jupyterhub.sqlite"
        # create a database connection
        conn = create_connection(database)
        addUser(conn,name)
    
main()

