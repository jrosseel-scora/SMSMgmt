import peewee
from peewee import *

scora_db = MySQLDatabase('scora_main_v2', user='scora', password='OpsDeploy88*',
                         host='192.168.49.24', port=3306)


class ScoraModel(Model):
    deleted = peewee.BooleanField()
    created = peewee.DateTimeField()
    lastmodified = peewee.DateTimeField()
    class Meta:
        database = scora_db  # This model uses the scora database

class ScoraSyncModel(ScoraModel):
    uuid = peewee.BinaryUUIDField()




