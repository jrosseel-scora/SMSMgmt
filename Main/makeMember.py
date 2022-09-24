
LIBRARIAN = 2
MUSICIAN = 3
OTHER_MEMBER = 4


member = {
    "librarian": 3,
    "musician": 2,
    "other": 4
}

member_query = (
    '''select 
          id, user_account_id, organization_account_id 
       from 
          member 
       where  `member`.`organization_account_id` = %s                 
    ''')


def getMemberId(dbConnection, userId, orchestraId):
    memberId_query = (
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
    existingmembercursor.execute(memberId_query, (userId, orchestraId))

    if existingmembercursor.rowcount == 0:
        # create new orchestra
        existingmembercursor.execute(insert_member_query, (userId, orchestraId))
        dbConnection.commit()
        existingmembercursor.execute(memberId_query, (userId, orchestraId))
        if existingmembercursor.rowcount == 0:
            return -1;

    row = existingmembercursor.fetchone()
    id = row[0]
    existingmembercursor.close()
    return id

def makeRoleId(dbConnection, memberId, roleId):
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
        return makeRoleId(dbConnection, memberId, roleId)
    else:
        row = existingmemberrolecursor.fetchone()
        id = row[0]
        existingmemberrolecursor.close()
        return id


def makeMember(dbConnection, accountId, groupId, roles):
    memberId = getMemberId(dbConnection, accountId, groupId)
    for role in roles:
        makeRoleId(dbConnection, memberId, role)
