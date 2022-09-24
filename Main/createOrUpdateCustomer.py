'''
Created on 18-dec.-2017

@author: Jan
'''

import mysql.connector
import unicodedata
from pyparsing import unicode

from Main import dbAccess
from Main import createOrUpdateAccount
from Main import passwords
from Main import makeMember

customer_query = (
    '''select
          id, firstname, lastname, company, adres, email, telephone
       from
          user_profile
       where `user_profile`.`email` = %s 
    ''' )

update_customer = (
    '''UPDATE 
            user_profile SET firstname = %s, lastname = %s, company = %s, adres = %s, email = %s, telephone = %s 
       where 
           `user_profile`.`id` = %s
       ''')
insert_new_customer = (
    '''INSERT INTO  
            user_profile (firstname, lastname, company, adres, email, telephone) 
        VALUES
            (%s, %s, %s, %s, %s, %s)
       ''')


def createOrUpdateCustomer(dbConnection, firstname, lastname, company, adres, email, telephone, oldEmail = None):
    if oldEmail == None:
        oldEmail = email

    print('Creating or updating customer ' + email)
    # orchestraId = getOrchestraId(orchestra, basedir, dbConnection)

    existingcustomercursor = dbConnection.cursor(buffered=True)
    existingcustomercursor.execute(customer_query, [oldEmail])
    if existingcustomercursor.rowcount == 0:
        existingcustomercursor.execute(insert_new_customer, (firstname, lastname, company, adres, email, telephone))
        dbConnection.commit()
        existingcustomercursor.execute(customer_query, [email])

    # should have customer record by now    
    row = existingcustomercursor.fetchone()
    customerId = row[0]

    updateNeeded = False
    if firstname != row[1] or lastname != row[2] or company != row[3] or adres != row[4] or email != row[5] or telephone != row[6]:
        existingcustomercursor.execute(update_customer, (firstname, lastname, company, adres, email, telephone, str(customerId)))
        dbConnection.commit()

    return customerId

def test1():
    dbConnection = mysql.connector.connect(user='root', password='lodetest',
                                           host='192.168.17.26',
                                           database='db_contentrights')

    id = createOrUpdateCustomer(dbConnection, 'Mieke', 'Vogels', 'Groen!', 'Ergens In, 2000 Antwerpen, Belgie', 'marieke.vogels@agalev.be', '+32 123456')

    print('created or returned ID = ' + str(id))

    id = createOrUpdateCustomer(dbConnection, 'Mieke', 'Vogels', 'Groen!', 'Ergens In, 2000 Antwerpen, Belgie', 'mieke.vogels@agalev.be', '+32 123456', 'marieke.vogels@agalev.be')

    print('modified email')

def strip_accents(text):
    # try:
    #     text = unicode(text, 'utf-8')
    # except NameError: # unicode is a default on python 3
    #     pass
    text = unicodedata.normalize('NFKD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode("utf-8")
    return str(text)

def createUserId(firstname, lastname):
    firstname = firstname.strip()
    lcFirst = firstname.lower()
    firstNoSpace = lcFirst.replace(' ', '')
    first = strip_accents(firstNoSpace)

    lastname = lastname.strip()
    lcLast = lastname.lower()
    lastNoSpace = lcLast.replace(' ', '')
    last = strip_accents(lastNoSpace)
    if len(first) > 0 and len(last) > 0:
        userId = first + '_' + last
    elif len(last) > 0:
        userId = last
    else:
        userId = first

    return userId

def createNewCustomer(firstname, lastname, company, adres, email, telephone, isDoble):

    musician = [makeMember.MUSICIAN]
    mastermusician = [makeMember.LIBRARIAN, makeMember.MUSICIAN]

    dbConnection = dbAccess.getDbConnection()

    if email is not None and len(email) > 0:
        customerId = createOrUpdateCustomer(dbConnection, firstname, lastname, company, adres, email, telephone)
    else:
        customerId = None

    userIdBase = createUserId(firstname, lastname)
    mainPwd = passwords.createPassword()

    mainAccountId = createOrUpdateAccount.createOrUpdateAccount(dbConnection, userIdBase, mainPwd, customerId, displayName = firstname + ' ' + lastname)

    if isDoble == True:
        groupId = userIdBase + '_group'
        groupPwd = passwords.createPassword()
        groupAccountId = createOrUpdateAccount.createOrUpdateAccount(dbConnection, groupId, groupPwd, customerId, accountType = 2)
        secondaryId = userIdBase + '_2'
        secondaryAccountId = createOrUpdateAccount.createOrUpdateAccount(dbConnection, secondaryId, mainPwd, customerId)
        makeMember.makeMember(dbConnection, mainAccountId, groupAccountId, mastermusician)
        makeMember.makeMember(dbConnection, secondaryAccountId, groupAccountId, musician)

    return mainAccountId

def test2():
    createNewCustomer('janneke', 'roske', 'squirrel', 'eenstraat 123, 4567 dddd, belgiek', 'me@myself.com', '0123456789', True)

# test2()