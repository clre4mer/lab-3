class NumError(Exception): #создаём исключение
    def __init__(self, text):
        self.txt = text

alfavit =  'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзиклмнопрстуфхцчшщъьэюяабвгдеёжзиклмнопрстуфхцчшщъьэюя'#русский алфавит
alfavitEng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'#английский алфавит
v=1
while v!=0:#цикл ввода с обработкой ошибок
    try:
        n=int(input(f'На каком языке будет зашифрованное сообщение?\n 1- Русский\n 2 - Английский\n'))
        if n>2 or n<1:
            raise NumError('Введённое число не соответствует вариантам выбора')

    except ValueError:
        print('Ошибка ввода данных, нужно ввести число')
        v=1
    except NumError as s:
        print('Ошибка ввода данных')
        print (s)
        v=1
    else:
        v=0
v=1
while v!=0:#цикл ввода с обработкой ошибок
    try:
        k = int(input("Введите отступ для шифрования:\n"))
    except ValueError:
        print('Ошибка ввода данных, нужно ввести число')
        v=1
    else:
        v=0
text = input('Введите текст для шифрования\n')
rez =''
if n==1:#ветвление в зависимости от выбранного языка
    if k>=33:
        while k >=33:
            k = k- 33
    for i in text:
        m1 = alfavit.find(i)
        m2 = m1 + k
        if i in alfavit:
            rez = rez + alfavit[m2]
        else:
            rez = rez + i
else:
    if k>=26:
        while k>=26:
            k = k - 26
    for i in text:
        m1 = alfavitEng.find(i)
        m2 = m1 + k
        if i in alfavitEng:
            rez = rez + alfavitEng[m2]
        else:
            rez = rez + i
print (rez)

