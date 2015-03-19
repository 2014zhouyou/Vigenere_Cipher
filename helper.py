import xlsxwriter
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

#judge a character
def isCharacter(a):
    if ((ord(a) >= 97 and ord(a) <= 122) or (ord(a) >= 65 and ord(a) <=90)):
        return True
    else:
        return False

#compute the index of coincidence of a text
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