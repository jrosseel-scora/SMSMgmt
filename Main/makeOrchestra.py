import csv
from collections import namedtuple

from Main import dbAccess
import Main.migrateDirectory
import Main.createOrUpdateCustomer
import Main.createOrUpdateAccount
import Main.makeMember
from Main import passwords


def createOrchestra(accountname, fullname):
    dbConnection = dbAccess.getDbConnection()
    mainPwd = passwords.createPassword()
    orchId = -1
    orchId = Main.createOrUpdateAccount.createOrUpdateAccount(dbConnection, accountname, mainPwd, None, displayName = fullname)
    return orchId

def createMusicians(musicianList, groupAccountId):
    dbConnection = dbAccess.getDbConnection()

    with open(musicianList, newline='') as f:
        reader = csv.reader(f, delimiter=';')

        headings = next(reader)
        Row = namedtuple('Row', headings)

        roleDict = Main.makeMember.member

        for r in reader:
            row = Row(*r)

            firstname = row.firstname
            lastname = row.lastname
            company = row.company
            address = row.address
            email = row.email
            telephone = row.telephone

            print(row)
            account = Main.createOrUpdateCustomer.createUserId(firstname, lastname)

            id = Main.createOrUpdateCustomer.createNewCustomer(firstname, lastname, company, address, email, telephone, False)
            roles = row.roles.split(',')
            roleIds = [roleDict[role] for role in roles]
            # for role in roles:
            #     role_id = roleDict[role]
            Main.makeMember.makeMember(dbConnection, id, groupAccountId, roleIds)

            # print(row)

#             if createUsers:
#                 createUser(users, row.musicianID, row.pwd, row.orchestra, row.instrument_eng, row.section, row.lead, 0)
#                 if row.backup == "1":
#                     createUser(users, row.musicianID + "_bak", row.pwd, row.orchestra, row.instrument_eng, row.section, row.lead, 1)
#
#             if apkPath:
# #                     scrollPref = Prefs.findGlobalPreference(row.musicianID, 'ScrollPage')
# #                     if scrollPref is not None and scrollPref == 'false':
#                 pushUpdateToUser(row.musicianID, apkPath)
#                 if row.backup == "1":
#                     pushUpdateToUser(row.musicianID + "_bak", apkPath)
#
#             if orchPath:
# #                    createUser(users, row.musicianID, row.pwd, row.orchestra, row.instrument_eng, row.section, row.lead, 0)
#                 prepareOrchestraMember(row.musicianID, orchPath, row.instrument_eng)
# #                     if row.backup == "1":
# #                         prepareOrchestraMember(row.musicianID + "_bak", orchPath, row.instrument_eng)
#
#             if partPath:
#                 pushPartToUser(row.musicianID, partPath, row.instrument_eng)
#                 if row.backup == "1":
#                     pushPartToUser(row.musicianID + "_bak", partPath, row.instrument_eng)
#
#             if playlistPath:
#                 pushPlaylistToUser(row.musicianID, playlistPath)
#                 if row.backup == "1":
#                     pushPlaylistToUser(row.musicianID + "_bak", playlistPath)
#
#             if createPDF:
#                 createPDFs(row.musicianID)
#
#             if mailPDF:
#                 sendPDFs(row.musicianID, row.naam, row.mail)
#
#             if moveAnnotsPath and not annotMoves is None:
#                 orchList.add(row.orchestra)
#                 moveAnnotationsForMusician(row.musicianID, annotMoves)
#
#             if restoreSourceDir:
#                 restorePrefs(row.musicianID, restoreSourceDir)



if __name__ == "__main__":
    orchId = createOrchestra("BB_TUC", "BigBand TU Clausthal")
    createMusicians("c:\\temp\\TU-Clausthal-members.csv", orchId)

