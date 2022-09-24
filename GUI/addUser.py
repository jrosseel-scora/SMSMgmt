from appJar import gui

from Main import createOrUpdateCustomer

app = gui()

def test():
    app = gui()
    app.addEntry("e1")
    app.addEntry("e2")
    app.addEntry("e3")
    app.addLabelEntry("Name")
    app.addValidationEntry("v1")
    app.addFileEntry("f1")

    app.setEntryDefault("e2", "Age here")
    app.setEntryValid("v1")

    app.go()

def addUser(btn):
    global app
    firstname = app.getEntry('FirstName')
    lastname = app.getEntry('LastName')
    company = app.getEntry('Company')
    address = app.getEntry('Address')
    zip = app.getEntry('zip')
    telephone = app.getEntry('Telephone')
    email = app.getEntry('MailAdress')
    app.getEntry('AccountId')
    isDoble  = app.getCheckBox('Doble')

    createOrUpdateCustomer.createNewCustomer(firstname, lastname, company, address, email, telephone, isDoble)
    pass


def addUserGUI():
    global app

    app.addLabelEntry('FirstName')
    app.addLabelEntry('LastName')
    app.addLabelEntry('Company')
    app.addLabelEntry('Address')
    app.addLabelEntry('zip')
    app.addLabelEntry('Telephone')
    app.addLabelEntry('MailAdress')
    app.addLabelEntry('AccountId')
    app.addCheckBox('Doble')

    app.addButton("Create", addUser)

    app.go()

addUserGUI()