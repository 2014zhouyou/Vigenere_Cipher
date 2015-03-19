import random
import xlsxwriter

SOURCE_FILE_NAME = 'Lord of the Rings.txt'
#generate a key according to length
def generateKey(length):
    key = ""
    for i in range(0, length):
        key = key + chr(random.randint(0,25) + 97)
    return key

#judge a character
def isCharacter(a):
    if ((ord(a) >= 97 and ord(a) <= 122) or (ord(a) >= 65 and ord(a) <=90)):
        return True
    else:
        return False

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

#remove the non-English Character from text
def trimText(text):
    result = ""
    for ch in text:
        if isCharacter(ch):
            result += ch
    return result

#compute the index of coincidence between the source text and encryption result
def indexOfCoincidence(text):
    sum = 0
    frequence_number = countFrequeceNumber(text)
    for i in range(0, 26):
        sum += frequence_number[i] * (frequence_number[i] - 1)

    character_length = len(trimText(text))
    return float(sum) / (character_length * (character_length - 1))

#write result to a excel sheet
def writeToSheet(length_of_key, en_frequency, de_frequency, coincidence_of_encrypt_result,
    coincidence_of_decrypt_result):
    workbook = xlsxwriter.Workbook('key-length' + str(length_of_key) + ".xlsx")
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 0, 'n = '+ str(length_of_key))

    col_head = "abcdefghijklmnopqrstuvwxyz"
    for i in range(0, 26):
        worksheet.write(1, i+1, col_head[i])
        worksheet.write(2, i+1, str(en_frequency[i]))
        worksheet.write(3, i+1, str(de_frequency[i]))

    worksheet.write(2, 0, '密文频率：')
    worksheet.write(3, 0, '明文频率：')

    worksheet.write(4, 0, '密文重合指数：')
    worksheet.write(4, 1, str(coincidence_of_encrypt_result))
    worksheet.write(5, 0, '明文重合指数：')
    worksheet.write(5, 1, str(coincidence_of_decrypt_result))

    workbook.close()

#the test function
def combineToTest():
    #generate key
    length_of_key = input("Please input the length of key:")
    key = generateKey(int(length_of_key))
    f_key = open("key.txt", "w")
    f_key.write(key)
    f_key.close()

    #read text
    fSource = open(SOURCE_FILE_NAME, 'r')
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


