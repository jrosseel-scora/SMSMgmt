from . import pyRandomdotOrg
from rdoclient_py3 import RandomOrgClient


def createPassword():
    r = RandomOrgClient("b1dff059-efa4-46cd-b921-300d2eb2ab44")
    pwd = r.generate_strings(1, 8, "23456789ABCDEFGHJKLMNPRSTUVWXYZabcdefghijkmnopqrstuvwxyz")
    # print(pwd)
    return pwd[0]

def createPassword_old():
    cl = pyRandomdotOrg.clientlib('ttt', 'me@myself.com')
    result = cl.RandomString(8)
    return result

