'''
Created on 11-apr.-2017

@author: Jan
'''

import mysql.connector

# user_query = (
#               '''select 
#                     id, username, password, base_dir, displayname 
#                  from 
#                     account 
#                  where `account`.`username` = %s                
#               ''' )
 
update_edition = (
               '''UPDATE 
                       edition SET creator_account_id = %s, score_dir = %s, released = %s
                  where 
                      `edition`.`id` = %s
                  ''')
# insert_new_user = (
#                '''INSERT INTO  
#                        account (username, password, accounttype_id, base_dir, displayname) 
#                    VALUES
#                        (%s, %s, %s, %s, %s)
#                   ''')


# def dummy():
# 
#     cnx = mysql.connector.connect(user='root', password='lodetest',
#                               host='192.168.17.26',
#                               database='db_contentrights')
# 
#     usercursor = cnx.cursor()
#     usercursor.execute(user_query, ['janr'])
#     for (id, username, password, base_dir, displayname ) in usercursor:
#         print('{} {}'.format(username, password))
#     usercursor.close()
#     
#     newuser = 'janv'
#     newpasswd = 'komkommer'
#     newbasedir = 'ftp://content.scora.net:52021'
#     newdisplayname = 'Jan Van Ceulebroeck'
#     newaccounttype = '1'
#     
# #         newusercursor = cnx.cursor()
# #         newusercursor.execute(insert_new_user, (newuser, newpasswd, newaccounttype, newbasedir, newdisplayname))
# #         cnx.commit()
# #         newusercursor.close()
# 
#     correctedbasedir = 'ftp://content.scora.net:53021'
#     updateusercursor = cnx.cursor()
#     updateusercursor.execute(update_user, (newuser, newpasswd, correctedbasedir, newdisplayname, newuser))
#     cnx.commit()
#     updateusercursor.close()

    
# def getOrchestraId(orchestra, basedir, dbConnection):
#     existingusercursor = dbConnection.cursor(buffered=True)
#     existingusercursor.execute(user_query, [orchestra])
#     if existingusercursor.rowcount == 0:
#         # create new orchestra
#         existingusercursor.execute(insert_new_user, (orchestra, 'somePWD', '2', basedir, orchestra))
#         dbConnection.commit()
#         existingusercursor.close()
#         return getOrchestraId(orchestra, basedir, dbConnection)
#     else:
#         row = existingusercursor.fetchone()
#         id = row[0]
#         existingusercursor.close()
#         return id    
    
# def getMemberId(userId, orchestraId, dbConnection):
#     member_query = (
#               '''select 
#                     id, user_account_id, organization_account_id 
#                  from 
#                     member 
#                  where `member`.`user_account_id` = %s  and `member`.`organization_account_id` = %s                 
#               ''' )
#     
#     insert_member_query = (
#                '''INSERT INTO  
#                        member (user_account_id, organization_account_id) 
#                    VALUES
#                        (%s, %s)
#                   ''')
#     
#     existingmembercursor = dbConnection.cursor(buffered=True)
#     existingmembercursor.execute(member_query, (userId, orchestraId))
#     
#     if existingmembercursor.rowcount == 0:
#         # create new orchestra
#         existingmembercursor.execute(insert_member_query, (userId, orchestraId))
#         dbConnection.commit()
#         existingmembercursor.close()
#         return getMemberId(userId, orchestraId, dbConnection)
#     else:
#         row = existingmembercursor.fetchone()
#         id = row[0]
#         existingmembercursor.close()
#         return id    
    
# def makeRoleId(memberId, roleId, dbConnection):
#     memberrole_query = (
#               '''select 
#                     member_id, role_id 
#                  from 
#                     member_role 
#                  where `member_role`.`member_id` = %s and `member_role`.`role_id` = %s             
#               ''' )
#     
#     insert_memberrole_query = (
#                '''INSERT INTO  
#                        member_role (member_id, role_id) 
#                    VALUES
#                        (%s, %s)
#                   ''')
#     
#     existingmemberrolecursor = dbConnection.cursor(buffered=True)
#     existingmemberrolecursor.execute(memberrole_query, (memberId, roleId))
#     
#     if existingmemberrolecursor.rowcount == 0:
#         # create new orchestra
#         existingmemberrolecursor.execute(insert_memberrole_query, (memberId, roleId))
#         dbConnection.commit()
#         existingmemberrolecursor.close()
#         return makeRoleId(memberId, roleId, dbConnection)
#     else:
#         row = existingmemberrolecursor.fetchone()
#         id = row[0]
#         existingmemberrolecursor.close()
#         return id    
    

def modifyEditionOwner(id, local_id, owner_id, url, released, dbConnection):

    print('Creating or updating edition ' + local_id) 
#     orchestraId = getOrchestraId(orchestra, basedir, dbConnection)
    
    cursor = dbConnection.cursor()
    cursor.execute(update_edition, (owner_id, url, released, id))
    dbConnection.commit()
    cursor.close()
    
#     if existingusercursor.rowcount == 0:
#         newpassword = password
#         newbasedir = basedir
#         existingusercursor.execute(insert_new_user, (username, password, '1', basedir, displayName))
#         dbConnection.commit()
#         existingusercursor.execute(user_query, [username])
# 
#     # should have user record by now    
#     row = existingusercursor.fetchone()
#     userId = row[0]
#     
#     updateNeeded = False
#     if password != row[2]:
#         updateNeeded = True
#         updatePwd = password
#     else:
#         updatePwd = row[2]
#     if basedir != row[3]:
#         updateNeeded = True
#         updateBaseDir = basedir
#     else:
#         updateBaseDir = row[3]
#     if displayName != row[4]:
#         updateNeeded = True
#         updateDisplayName = displayName
#     else:
#         updateDisplayName = row[4]
#         
#     if (updateNeeded):
#         existingusercursor.execute(update_user, (username, updatePwd, updateBaseDir, updateDisplayName, username))
#     
#     # create orchestra membership (if it odes not exist)
#     memberId = getMemberId(userId, orchestraId, dbConnection)
#     # create role (if it does not exist)
#     makeRoleId(memberId, role, dbConnection)
#     
#     return userId
 
    
    