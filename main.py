import passwordGeneration
import PasswordStorageAndRetrevial

password = passwordGeneration.generatePassword();
userName = "HelloWorld";
passwordDict = dict()
passwordDict["test.com"] = [userName, password]
PasswordStorageAndRetrevial.writePasswordSet(userName, passwordDict)
print(PasswordStorageAndRetrevial.readPasswordSet(userName))
