import random

def verifyPassword(passwordCanidate, upperCase, lowerCase, number, special):
    for i in passwordCanidate:
        if i.isalpha():
            if i.isupper():
                upperCase -= 1
            else:
                lowerCase -= 1
        elif i.isnumeric():
            number -= 1
        else:
            special -= 1
    return upperCase <= 0 and lowerCase <= 0 and number <= 0 and special <= 0

def generatePassword(minUpperCase = 0, minLowercase = 0, minNum = 0, minSpecial = 0, minLength = 32, maxLength = 32):
    passList = []
    i = 0;
    while i < 1000:
        while True:
            if len(passList) > minLength and random.randint(0,100) > 90 :
                break;
            else:
                det = random.randint(0,100)
                if det < 20:
                    passList.append(chr(random.randint(33,47)))
                elif det < 40:
                    passList.append(chr(random.randint(48,57)))
                elif det < 80:
                    passList.append(chr(random.randint(65,90)))
                else:
                    passList.append(chr(random.randint(97,122)))
            if len(passList) == maxLength:
                break;
        if verifyPassword(passList, minUpperCase, minLowercase, minNum, minSpecial):
            break
        else:
            i+=1
    return ''.join(passList)


