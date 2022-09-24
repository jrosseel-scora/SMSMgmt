'''
Created on 10-apr.-2017

@author: Jan
'''

import csv
from collections import namedtuple

import Main.migrateDirectory
import Main.createOrUpdateUser

def processCSV(musicianList, commands, dbConnection):
    with open(musicianList, newline='') as f:
        reader = csv.reader(f,delimiter=';')
        
        headings = next(reader)
        Row = namedtuple('Row', headings)
        
        for r in reader:
            row = Row(*r)
            
            
            print('naam: ' + row.username + ' paswoord: ' + row.password  + ' orch: ' + row.orchestra  + ' role: ' + row.role  + ' basedir: ' + row.basedir)
            
            for command in commands:
                if command == 'createOrUpdate':
                    Main.createOrUpdateUser.createOrUpdateUser(row.username, row.password, row.orchestra, row.role, row.basedir, row.displayName, dbConnection)
                elif command == 'migrate':
                    Main.migrateDirectory.migrateDirectory(row.username, dbConnection)
                    
            
            
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
    
