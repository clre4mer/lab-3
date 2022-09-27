alfavit =  'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзиклмнопрстуфхцчшщъьэюяабвгдеёжзиклмнопрстуфхцчшщъьэюя'
text = input("Введите текст для шифрования:\n")
k = int(input("Введите отступ для шифрования:\n"))
rez =''
for i in text:
    m1 = alfavit.find(i)
    m2 = m1 + k
    if i in alfavit:
        rez = rez + alfavit[m2]
    else:
        rez = rez + i
print (rez)

