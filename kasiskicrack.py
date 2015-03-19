#import some function
from helper import indexOfCoincidence
from helper import trimText
from helper import countFrequency

#some constants
STANDARD_INDEX_OF_COINCIDENCE = 0.065
ACCEPT_CASE = 0.005
FREQUENCE_TABLE = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094, 0.06966, 0.00153, 0.00772
,0.04025, 0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758, 0.00978, 0.02360, 0.00150
,0.01974, 0.00074]
#compute the key's length
def getKeyLength(encrypt_text):
    print("Getting the length of key...")
    key_length = 3
    while True:
        key_length += 1
        flag = False
        encrypt_lengthed_string = getLengthedString(key_length, encrypt_text)
        index_of_coincidence = []
        for text in encrypt_lengthed_string:
            index_of_coincidence.append(indexOfCoincidence(text))
        for item in index_of_coincidence:
            if abs(item - STANDARD_INDEX_OF_COINCIDENCE) > ACCEPT_CASE:
                flag = True
        if flag:
            continue
        else:
            break
    print("Getting the key's length successfully!")
    return key_length

#divide the text into group according to length
def getLengthedString(length, text):
    result = [''] * length
    handled_text = trimText(text)
    for i in range(0, len(handled_text)):
        result[i % length] += handled_text[i]
    return result

#the main part to get the key
def findKey(key_length, encrypt_text):
    print("Finding the key...")
    encrypt_lengthed_string = getLengthedString(key_length, encrypt_text)
    key = ""
    for keyI in range(0, len(encrypt_lengthed_string)):
        ch = findMaxFrequencyCharacter(encrypt_lengthed_string[keyI])
        key += computeSingleKeyCharacter(ch)
    print("Finding the key successfully!")
    return key

#the main part to crack a Vigenere Cipher according to encrypt text
def cracker():
    encrypt_file_name = input("Please input the encrypted(using Vigenere Cipher) file name:")
    print("Start of Crack")
    f_encrypt_text = open(encrypt_file_name)
    encrypt_text = f_encrypt_text.read()
    f_encrypt_text.close()
    key_length = getKeyLength(encrypt_text)
    key = findKey(key_length, encrypt_text)
    print("The key is '" + key + "'")
    print("End of Processing")

#find the max frequency character
def findMaxFrequencyCharacter(text):
    frequency_text = countFrequency(text)
    max = 0
    for index in range(0, len(frequency_text)):
        if frequency_text[index] >= frequency_text[max]:
            max = index
    return chr(max + 97)

#compute the single key character
def computeSingleKeyCharacter(ch):
    #print(ch)
    if ord('e') <= ord(ch):
        return chr((ord(ch)  -  ord('e')) + 97)
    else:
        return chr((ord(ch) + 26 - 1 - ord('e')) + 97)

cracker()
