import peewee

from db import ScoraModel, ScoraSyncModel

class AccountType(ScoraModel):
    id = peewee.AutoField()
    description = peewee.TextField()
    class Meta:
        table_name = 'accounttype'

class User(ScoraModel):
    id = peewee.AutoField()
    firstname = peewee.TextField()
    lastname = peewee.TextField()
    address = peewee.TextField(column_name='adres')
    telephone = peewee.TextField()
    email = peewee.TextField()
    company = peewee.TextField()
    class Meta:
        table_name = 'user_profile'


class Account(ScoraSyncModel):
    id = peewee.AutoField()
    type = peewee.ForeignKeyField(AccountType, column_name='accounttype_id')
    username = peewee.TextField()
    password = peewee.TextField()
    displayname = peewee.TextField()
    user = peewee.ForeignKeyField(User, column_name='user_profile_id', null=True)


if __name__ == '__main__':
    allAccounts = Account.select()
    for account in allAccounts:
        type = account.type
        user = account.user
        print(account.id, account.displayname, type.description, f"{user.firstname} {user.lastname}" if user is not None else user)
