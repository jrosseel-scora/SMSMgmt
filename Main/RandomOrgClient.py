from rdoclient_py3 import RandomOrgClient


r = RandomOrgClient("133808ce-f544-4d81-84bf-b8d77617ed54")
# l = r.generate_integers(5, 0, 10)
# print(l)
pwd = r.generate_strings(1, 8, "23456789ABCDEFGHJKLMNPRSTUVWXYZabcdefghijkmnopqrstuvwxyz")
print(pwd)
