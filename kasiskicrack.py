STANDARD_INDEX_OF_COINCIDENCE = 0.065
ACCEPT_CASE = 0.005
FREQUENCE_TABLE = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094, 0.06966, 0.00153, 0.00772
,0.04025, 0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758, 0.00978, 0.02360, 0.00150
,0.01974, 0.00074]
#compute the key's length
def getKeyLength(encrypt_text):
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
        print(flag)
        if flag:
            continue
        else:
            break

    return key_length

#compute the coincidence of the text
def indexOfCoincidence(text):
    sum = 0
    frequence_number = countFrequeceNumber(text)
    for i in range(0, 26):
        sum += frequence_number[i] * (frequence_number[i] - 1)

    character_length = len(trimText(text))
    return float(sum) / (character_length * (character_length - 1))

#judge a character
def isCharacter(a):
    if ((ord(a) >= 97 and ord(a) <= 122) or (ord(a) >= 65 and ord(a) <=90)):
        return True
    else:
        return False

#remove the non-English Character from text
def trimText(text):
    result = ""
    for ch in text:
        if isCharacter(ch):
            result += ch
    return result

#divide the text into group according to length
def getLengthedString(length, text):
    result = [''] * length
    handled_text = trimText(text)
    for i in range(0, len(handled_text)):
        result[i % length] += handled_text[i]
    return result

#count the frequency number of  character
def countFrequeceNumber(text):
    result = [0] * 26
    text = text.lower()
    for ch in text:
        if (isCharacter(ch)):
            result[ord(ch) - 97] = result[ord(ch) - 97] + 1
    return result

#count the frequency of character
def countFrequency(text):
    frequence_number = countFrequeceNumber(text)
    frequency = []
    length_of_character = len(trimText(text))
    for i in range(0, 26):
        frequency.append(float("%.4f" % (frequence_number[i] / length_of_character)))
    return frequency

#the main part to get the key
def findKey(key_length, encrypt_text):
    print("Into findkey:")
    encrypt_lengthed_string = getLengthedString(key_length, encrypt_text)
    key = ""
    for keyI in range(0, len(encrypt_lengthed_string)):
        print(countFrequency(encrypt_lengthed_string[keyI]))
        ch = findMaxFrequencyCharacter(encrypt_lengthed_string[keyI])
        key += computeSingleKeyCharacter(ch)
    return key

#shit a text for the purpose of guess key
def shiftN(shift_n, text):
    shift_result = ""
    for ch in text:
        if (ord(ch) - shift_n) < 97:
            shift_result += chr((ord(ch)  - shift_n) + 26)
        else:
            shift_result += chr((ord(ch) - shift_n))
    return shift_result

#check whether the shift is correct
def validate(text):
    frequency_of_text = countFrequency(text)
    sum = 0
    for index in range(0, 26):
        sum = sum + frequency_of_text[index] * FREQUENCE_TABLE[index]
    if abs((sum - STANDARD_INDEX_OF_COINCIDENCE)) <= ACCEPT_CASE:
        return True
    else:
        return False

#the main part to crack a Vigenere Cipher according to encrypt text
def cracker():
    f_encrypt_text = open("encrypt.txt")
    encrypt_text = f_encrypt_text.read()
    f_encrypt_text.close()
    key_length = getKeyLength(encrypt_text)
    key = findKey(key_length, encrypt_text)
    print("The key is " + key)

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
