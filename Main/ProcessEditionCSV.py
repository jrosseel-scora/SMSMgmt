'''
Created on 11-apr.-2017

@author: Jan
'''

'''
Created on 10-apr.-2017

@author: Jan
'''

import csv
from collections import namedtuple

# import Main.migrateDirectory
import Main.modifyEditionOwner

def processCSV(editionList, commands, dbConnection):
    with open(editionList, newline='') as f:
        reader = csv.reader(f,delimiter=';')
        
        headings = next(reader)
        Row = namedtuple('Row', headings)
        
        for r in reader:
            row = Row(*r)
            
            if row.released == '1':
                releasedString = 'Yes'
            elif row.released == '0':
                releasedString = 'No'
            else:
                releasedString = 'undetermined'
            
            print('DB id: ' + row.id + ' local ID: ' + row.local_id  + ' new owner: ' + row.owner_id  + ' URL: ' + row.url + ' released' + releasedString)
            
            for command in commands:
                if command == 'ModifyOwner':
                    Main.modifyEditionOwner.modifyEditionOwner(row.id, row.local_id, row.owner_id, row.url, row.released, dbConnection)
#                 elif command == 'migrate':
#                     Main.migrateDirectory.migrateDirectory(row.username, dbConnection)
                    
            
            
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
    
