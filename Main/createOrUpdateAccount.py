'''
Created on 10-apr.-2017

@author: Jan
'''

import mysql.connector

from . import makeMember

account_query = (
              '''select 
                    id, username, password, base_dir, displayname 
                 from 
                    account 
                 where `account`.`username` = %s                
              ''' )
 
update_account = (
               '''UPDATE 
                       account SET username = %s, password = %s, base_dir = %s, displayname = %s, accounttype_id = %s, user_profile_id = %s
                  where 
                      `account`.`username` = %s
                  ''')
insert_new_account = (
               '''INSERT INTO  
                       account (username, password, accounttype_id, base_dir, displayname, user_profile_id) 
                   VALUES
                       (%s, %s, %s, %s, %s, %s)
                  ''')

SCORA_GROUP = 3

def dummy():

    cnx = mysql.connector.connect(user='root', password='lodetest',
                              host='192.168.17.26',
                              database='db_contentrights')

    usercursor = cnx.cursor()
    usercursor.execute(account_query, ['janr'])
    for (id, username, password, base_dir, displayname ) in usercursor:
        print('{} {}'.format(username, password))
    usercursor.close()
    
    newuser = 'janv'
    newpasswd = 'komkommer'
    newbasedir = 'ftp://content.scora.net:52021'
    newdisplayname = 'Jan Van Ceulebroeck'
    newaccounttype = '1'
    
#         newusercursor = cnx.cursor()
#         newusercursor.execute(insert_new_user, (newuser, newpasswd, newaccounttype, newbasedir, newdisplayname))
#         cnx.commit()
#         newusercursor.close()

    correctedbasedir = 'ftp://content.scora.net:53021'
    updateusercursor = cnx.cursor()
    updateusercursor.execute(update_account, (newuser, newpasswd, correctedbasedir, newdisplayname, newuser))
    cnx.commit()
    updateusercursor.close()

    
def getOrchestraId(orchestra, basedir, dbConnection):
    existingusercursor = dbConnection.cursor(buffered=True)
    existingusercursor.execute(account_query, [orchestra])
    if existingusercursor.rowcount == 0:
        # create new orchestra
        existingusercursor.execute(insert_new_account, (orchestra, 'somePWD', '2', basedir, orchestra))
        dbConnection.commit()
        existingusercursor.close()
        return getOrchestraId(orchestra, basedir, dbConnection)
    else:
        row = existingusercursor.fetchone()
        id = row[0]
        existingusercursor.close()
        return id    
    
def getMemberId(userId, orchestraId, dbConnection):
    member_query = (
              '''select 
                    id, user_account_id, organization_account_id 
                 from 
                    member 
                 where `member`.`user_account_id` = %s  and `member`.`organization_account_id` = %s                 
              ''' )
    
    insert_member_query = (
               '''INSERT INTO  
                       member (user_account_id, organization_account_id) 
                   VALUES
                       (%s, %s)
                  ''')
    
    existingmembercursor = dbConnection.cursor(buffered=True)
    existingmembercursor.execute(member_query, (userId, orchestraId))
    
    if existingmembercursor.rowcount == 0:
        # create new orchestra
        existingmembercursor.execute(insert_member_query, (userId, orchestraId))
        dbConnection.commit()
        existingmembercursor.close()
        return getMemberId(userId, orchestraId, dbConnection)
    else:
        row = existingmembercursor.fetchone()
        id = row[0]
        existingmembercursor.close()
        return id    
    
def makeRoleId(memberId, roleId, dbConnection):
    memberrole_query = (
              '''select 
                    member_id, role_id 
                 from 
                    member_role 
                 where `member_role`.`member_id` = %s and `member_role`.`role_id` = %s             
              ''' )
    
    insert_memberrole_query = (
               '''INSERT INTO  
                       member_role (member_id, role_id) 
                   VALUES
                       (%s, %s)
                  ''')
    
    existingmemberrolecursor = dbConnection.cursor(buffered=True)
    existingmemberrolecursor.execute(memberrole_query, (memberId, roleId))
    
    if existingmemberrolecursor.rowcount == 0:
        # create new orchestra
        existingmemberrolecursor.execute(insert_memberrole_query, (memberId, roleId))
        dbConnection.commit()
        existingmemberrolecursor.close()
        return makeRoleId(memberId, roleId, dbConnection)
    else:
        row = existingmemberrolecursor.fetchone()
        id = row[0]
        existingmemberrolecursor.close()
        return id    
    

def createOrUpdateAccount(dbConnection, username, password, customerId = '', baseDir = 'ftp://content.scora.net:53021', displayName = '', accountType = 1):

    if baseDir == None:
        basedir = 'ftp://content.scora.net:53021'

    print('Creating or updating user ' + username) 
    # orchestraId = getOrchestraId(orchestra, basedir, dbConnection)
    
    existingusercursor = dbConnection.cursor(buffered=True)

    newAccount = False
    existingusercursor.execute(account_query, [username])
    if existingusercursor.rowcount == 0:
        existingusercursor.execute(insert_new_account, (username, password, accountType, baseDir, displayName, customerId))
        dbConnection.commit()
        existingusercursor.execute(account_query, [username])
        newAccount = True

    # should have user record by now    
    row = existingusercursor.fetchone()
    userId = row[0]
    
    updateNeeded = False
    if password != row[2]:
        updateNeeded = True
        updatePwd = password
    else:
        updatePwd = row[2]
    if baseDir != row[3]:
        updateNeeded = True
        updateBaseDir = basedir
    else:
        updateBaseDir = row[3]
    if displayName != row[4]:
        updateNeeded = True
        updateDisplayName = displayName
    else:
        updateDisplayName = row[4]
        
    if (updateNeeded):
        existingusercursor.execute(update_account, (username, updatePwd, updateBaseDir, updateDisplayName, accountType, customerId, username))
        dbConnection.commit()

    if newAccount == True:
        makeMember.makeMember(dbConnection, userId, SCORA_GROUP, [makeMember.OTHER_MEMBER])

    # # create orchestra membership (if it odes not exist)
    # memberId = getMemberId(userId, orchestraId, dbConnection)
    # # create role (if it does not exist)
    # makeRoleId(memberId, role, dbConnection)
    
    return userId


    