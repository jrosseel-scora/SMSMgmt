import peewee

from db import ScoraModel

from account import Account

class Role(ScoraModel):
    id = peewee.AutoField()
    name = peewee.TextField()
    class Meta:
        table_name = 'roletype'

class Member(ScoraModel):
    id = peewee.AutoField()
    account = peewee.ForeignKeyField(Account, column_name='user_account_id')
    ensemble = peewee.ForeignKeyField(Account, column_name='organization_account_id', backref='members')

class MemberRole(ScoraModel):
    id = peewee.AutoField(column_name='autoId')
    member = peewee.ForeignKeyField(Member, column_name='member_id')
    role = peewee.ForeignKeyField(Role, column_name='role_id')
    class Meta:
        table_name = 'member_role'

if __name__ == '__main__':
    # allAccounts = Account.select().where(Account.type == 2)
    allAccounts = Account.select().where(Account.id == 523)
    for account in allAccounts:
        type = account.type
        user = account.user
        print(account.id, account.displayname, type.description, f"{user.firstname} {user.lastname}" if user is not None else user)
        for member in account.members:
            print(f"\t{member.account.id:3d} {member.account.displayname}")
            print(f"\t\tMember id: {member.id}")
            for memberrole in member.memberrole_set:
                print(f"\t\t{memberrole.id} {memberrole.role.name}")
        # for member in account.member_set:
        #     print(member)
