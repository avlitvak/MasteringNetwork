services = {'ftp':21,'ssh':22, 'smtp':25, 'http':80}
services2 = {'snmp':161, 'ldap':389, 'ftp':21, 'ssh':22}
print(services)
services.update(services2)
print(services)

def contains(sequence,item):
    
    for element in sequence:
        if element == item:
            return True

    return False

print(contains([100, 200, 300, 400], 200))

print(contains(services, 'ftps'))