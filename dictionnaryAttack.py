import sys
import hashlib

def loadFile(filename):
    file = open(filename,"r")
    array = []
    for line in file:
        array.append(line.replace('\n',''))
    file.close()
    return array

def crack_sha1_hash(hash):
    passwords = loadFile("words.txt")
    value = "PASSWORD NOT IN DATABASE"
    for line in passwords:
        currentPass = line.replace('\n','')
        if hashlib.sha1(currentPass.encode()).hexdigest() == hash:
            value = currentPass
            break
    return value

if __name__ == "__main__":
    print(crack_sha1_hash(sys.argv[1]))
