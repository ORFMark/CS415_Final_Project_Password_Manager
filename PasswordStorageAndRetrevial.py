import re
def readPasswordSet(username):
    passwordDictionary = dict()
    f = open(username + ".txt", 'r')
    lines = f.readlines()
    for i in lines:
        info = re.split(":", i)
        passwordDictionary[info[0]] = [info[1], info[2]]
    f.close()
    return passwordDictionary


def writePasswordSet(username, set):
    f = open(username + ".txt", 'w')
    for i in set.keys():
        f.write(i + ":" + set[i][0] + ":" + set[i][1])
    f.close()
