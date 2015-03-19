from helper import *
import random

SOURCE_FILE_NAME = 'Lord of the Rings.txt'
#generate a key according to length
def generateKey(length):
    key = ""
    for i in range(0, length):
        key = key + chr(random.randint(0,25) + 97)
    return key

# return the row of k, col of c in the encryption table
def encryptSingle(c, k):
    return chr((ord(c) - 97 + ord(k) - ord('a')) % 26 + 97)

#decrypt a single character according to the decryption table
def decryptSingle(m, k):
    if ord(m) >= ord(k):
        return chr(ord(m) - ord(k) + 97)
    else:
        return chr(ord('z') - ord(k) + 1 + ord(m))

#encrypt a text or decrypt a text
def action(source_text, key, algorithm):
    target_text = ""
    source_text = source_text.lower()
    length_of_key = len(key)
    count = -1
    for ch in source_text:
        if isCharacter(ch):
            count += 1
            ch = algorithm(ch, key[count % length_of_key])
        target_text = target_text + ch
    return target_text

#the test function
def combineToTest():
    #generate key
    source_file_name = input("Please input the source file name:")
    length_of_key = input("Please input the length of key:")
    key = generateKey(int(length_of_key))
    f_key = open("key.txt", "w")
    f_key.write(key)
    f_key.close()

    #read text
    fSource = open(source_file_name, 'r')
    source_text = fSource.read()
    fSource.close()

    #encrypt and decrypt
    encrypt_result = action(source_text, key, encryptSingle)
    decrypt_result = action(encrypt_result, key, decryptSingle)

    f_encrypt = open("encrypt.txt", "w")
    f_encrypt.write(encrypt_result)
    f_encrypt.close()

    f_decrypt = open("decrypt.txt", "w")
    f_decrypt.write(decrypt_result)
    f_decrypt.close()

    #count the frequency of encrypt result and decrypt result
    #for encrypt text
    print("when n = " + str(length_of_key))
    #en_frequence_number = countFrequeceNumber(encrypt_result)
    en_frequency = countFrequency(encrypt_result)
    print("frequency of encrypt result:" +  "\n" + str(en_frequency))
    #for decrypt text
    #de_frequence_number = countFrequeceNumber(decrypt_result)
    de_frequency = countFrequency(decrypt_result)
    print ("frequency of decrypt result:" + "\n" + str(de_frequency))

    #compute the index of coincidence
    coincidence_of_encrypt_result = indexOfCoincidence(encrypt_result)
    coincidence_of_decrypt_result = indexOfCoincidence(decrypt_result)
    print("n = " + str(length_of_key))
    print("The index of coincidence of encrypt result: " + ("%.4f" % coincidence_of_encrypt_result))
    print("The index of coincidence of decrypt result: " + ("%.4f" % coincidence_of_decrypt_result))

    writeToSheet(length_of_key, en_frequency, de_frequency, coincidence_of_encrypt_result,
                 coincidence_of_decrypt_result)

    print("Process successfully!")

combineToTest()

