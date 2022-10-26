# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

with open('file_encode.txt', 'r') as data:
    txt1 = data.read()    

def encoding(txt1):
    count = ''
    b = '' 
    result = ''
    for i in txt1:
        if i == b: 
            count += 1  
        else:
            result += b + str(count)                        
            count = 1 
            b = i 
    result += b + str(count)    
    
    return result 

with open('file_decode.txt', 'r') as data:
    txt2 = data.read()    

def decoding(txt2):
    decode = ''
    count = ''
    for char in txt2:

        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode

    
print(f"Текст после кодировки: {encoding(txt1)}")
print(f"Текст после дешифровки: {decoding(txt2)}")
