import hashlib

def loadFile(filename):
    file = open(filename,"r")
    array = []
    for line in file:
        array.append(line.replace('\n',''))
    file.close()
    return array

def crack_with_salt(hash, passwords, salts):
    for password in passwords:
        for salt in salts:
            SaltAndPass = salt + password
            PassAndSalt = password + salt
            if hashlib.sha1(SaltAndPass.encode()).hexdigest() == hash or\
               hashlib.sha1(PassAndSalt.encode()).hexdigest() == hash :
                return password
    return "PASSWORD NOT IN DATABASE"

def crack_without_salt(hash, passwords):
    pass

def crack_sha1_hash(hash, use_salts=False):
    passwords = loadFile("top-10000-passwords.txt")
    value = "PASSWORD NOT IN DATABASE"
    if use_salts:
        salts = loadFile("known-salts.txt")
        value = crack_with_salt(hash, passwords, salts)
    else:
        for line in passwords:
            currentPass = line.replace('\n','')
            if hashlib.sha1(currentPass.encode()).hexdigest() == hash:
                value = currentPass
                break
    return value