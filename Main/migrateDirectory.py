'''
Created on 10-apr.-2017

@author: Jan
'''

import os
import shutil
import mysql.connector



sourcedir = 'S:\WOIContent\Musicians'
targetdir = 'S:\WOIContent\DBMusicians'

def migrateDirectory(username, dbConnection):

    user_query = (
              '''select 
                    id, username, password, base_dir, displayname 
                 from 
                    account 
                 where `account`.`username` = %s                
              ''' )


    cursor = dbConnection.cursor(buffered=True)
    cursor.execute(user_query, [username])
    
    if cursor.rowcount == 0:
        print('user ' + username + ' not found in DB') 
        return

    row = cursor.fetchone()
    ID = row[0]     
    print('user ' + username + ' found in DB with id ' + str(ID) + ' . Migrating key directories') 
    
    usersourcedir = os.path.join(sourcedir, username)
    if not os.path.isdir(usersourcedir):
        print ('No source dir for user ' + username)
        return
    
    usertargetdir = os.path.join(targetdir, str(ID))
    try:
        os.mkdir(usertargetdir)
    except Exception as e:
        print('Cannot migrate directories for user ' + username + '. directory already exists')
        return

    
    for subdir in ('Annotations', 'Prefs'):
        sourcesubdirpath = os.path.join(usersourcedir, subdir)
        targetsubdirpath = os.path.join(usertargetdir, subdir)
        shutil.copytree(sourcesubdirpath, targetsubdirpath)
    
