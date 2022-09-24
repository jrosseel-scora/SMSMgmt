#!/usr/local/bin/python2.7
# encoding: utf-8
'''
Main.main -- shortdesc

Main.main is a description

It defines classes_and_methods

@author:     user_name

@copyright:  2017 organization_name. All rights reserved.

@license:    license

@contact:    user_email
@deffield    updated: Updated
'''

import sys
import os

from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter

import mysql.connector

import Main.createOrUpdateUser
import Main.migrateDirectory
import Main.ProcessEditionCSV
import Main.ProcessAccountCSV

__all__ = []
__version__ = 0.1
__date__ = '2017-04-08'
__updated__ = '2017-04-08'

DEBUG = 0
TESTRUN = 0
PROFILE = 0

class CLIError(Exception):
    '''Generic exception to raise and log different fatal errors.'''
    def __init__(self, msg):
        super(CLIError).__init__(type(self))
        self.msg = "E: %s" % msg
    def __str__(self):
        return self.msg
    def __unicode__(self):
        return self.msg

def main(argv=None): # IGNORE:C0111
    '''Command line options.'''

    if argv is None:
        argv = sys.argv
    else:
        sys.argv.extend(argv)

    program_name = os.path.basename(sys.argv[0])
    program_version = "v%s" % __version__
    program_build_date = str(__updated__)
    program_version_message = '%%(prog)s %s (%s)' % (program_version, program_build_date)
    program_shortdesc = __import__('__main__').__doc__.split("\n")[1]
    program_license = '''%s

  Created by user_name on %s.
  Copyright 2017 organization_name. All rights reserved.

  Licensed under the Apache License 2.0
  http://www.apache.org/licenses/LICENSE-2.0

  Distributed on an "AS IS" basis without warranties
  or conditions of any kind, either express or implied.

USAGE
''' % (program_shortdesc, str(__date__))

    try:
        # Setup argument parser
#         parser = ArgumentParser(description=program_license, formatter_class=RawDescriptionHelpFormatter)
#         parser.add_argument(dest="csvFile", help="Path to CSV file containing user info")
# 
#         # Process arguments
#         args = parser.parse_args()

#         csvFilePath = args.csvFile

        
    #     cursor = cnx.cursor()
    
    #    cursor.execute (add_musician, data_musician)
    #    musicianid = cursor.lastrowid
    #    cnx.commit()
    
    
        
    #     rows = cursor.fetchall()
    #     
    #     for (edition_id, publisher, scoredir, start_date, end_date, vvv) in rows:
    #         print("{} {} {} {} {} {}".format(edition_id, publisher, scoredir, start_date, end_date, vvv))
    #             
    #     cursor.close()
#         usercursor.close()
#         cnx.close()
    
        
        dbConnection = mysql.connector.connect(user='root', password='lodetest',
                              host='192.168.17.26',
                              database='db_contentrights')

#         Main.createOrUpdateUser.createOrUpdateUser('testje', 'testje', 'wiener_sager_knaben', '2', 'somebasedir', 'Just a Test', dbConnection)
#         Main.migrateDirectory.migrateDirectory('janr', dbConnection)
        Main.ProcessAccountCSV.processCSV("c:\\temp\\migrate_lao_2.csv", ['createOrUpdate'], dbConnection)
#         Main.ProcessAccountCSV.processCSV("c:\\temp\\migrate_lao.csv", ('createOrUpdate', 'migrate'), dbConnection)
#         Main.ProcessEditionCSV.processCSV("c:\\temp\\migrateEditions.csv", ['ModifyOwner'], dbConnection)
        

        return 0
    except KeyboardInterrupt:
        ### handle keyboard interrupt ###
        return 0
    except Exception as e:
        if DEBUG or TESTRUN:
            raise(e)
        indent = len(program_name) * " "
        sys.stderr.write(program_name + ": " + repr(e) + "\n")
        sys.stderr.write(indent + "  for help use --help")
        return 2

if __name__ == "__main__":
    if DEBUG:
        sys.argv.append("-h")
        sys.argv.append("-v")
        sys.argv.append("-r")
    if TESTRUN:
        import doctest
        doctest.testmod()
    if PROFILE:
        import cProfile
        import pstats
        profile_filename = 'Main.main_profile.txt'
        cProfile.run('main()', profile_filename)
        statsfile = open("profile_stats.txt", "wb")
        p = pstats.Stats(profile_filename, stream=statsfile)
        stats = p.strip_dirs().sort_stats('cumulative')
        stats.print_stats()
        statsfile.close()
        sys.exit(0)
    sys.exit(main())