
import mysql.connector

def getDbConnection():
    dbConnection = mysql.connector.connect(user='scora', password='OpsDeploy88*',
                                           host='192.168.49.24',
                                           database='scora_main_v2')
    return dbConnection