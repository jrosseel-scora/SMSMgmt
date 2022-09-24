
from peewee import *
from playhouse.mysql_ext import MySQLConnectorDatabase

db = MySQLConnectorDatabase('scora_main_v2', host = '192.168.49.24', user = 'scora', password = 'OpsDeploy88*ddddddd')

class Edition(Model):
    uuid = UUIDField()
    orgId = IntegerField(column_name="creator_account_id")

    class Meta:
        database = db

class Tag(Model):
    uuid = UUIDField()
    orgId = IntegerField(column_name="creator_account_id")
    tag_type = IntegerField(column_name="tagtype_id")

    class Meta:
        database = db



class EditionTag(Model):
    edition_uuid = UUIDField()
    tag_uuid = UUIDField()
    owner_id = IntegerField(column_name="creator_account_id")

    class Meta:
        table_name = "edition_tag"
        database = db





















def updateOrganizationEditions(organizationId):
    pass
    # find org tag
    # tags = Tag.select().where(Tag.orgId == organizationId)
    tags = Tag.select()
    if tags is None:
        return
    for tag in tags:
        print(tag)
    # list editions for org & iterate

        # for every edition, see if there is a matching tag
        # if yes, leave it alone (do not change deleted!)
        # if not, add it









if __name__ == "__main__":
    db.connect()
    orgs = [20]
    for org in orgs:
        updateOrganizationEditions(org)
    db.close()