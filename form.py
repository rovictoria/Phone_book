names = ['Иванов А.А', 'Петров Б.Б', 'Серов В.В.']
phones = ['+79922293773\n','+799922298338\n','+79937287383\n']

def Add_phone():
    global names
    global phones

    name = input("Введите ФИО: ")
    new_phone = input("Введите номер телефона через +7: ") + '\n'

    names.append(name)
    phones.append(new_phone)
    return 'Файл обновлен, нажмите кнопку -Вывести справочник-'

def Print_phones():
    global names
    global phones

    list =[]
    for i in range(len(names)):
        list.append(names[i])
        list.append(phones[i])

    return ' '.join(list)

def Save_as_html():
    global names
    global tel

    book = open('my_book.html', 'w', encoding='utf-8')
    for i in range(len(names)):
        book.write(names[i])
        book.write(' ')
        book.write(phones[i])

    return 'Файл "my_book.html" сохранен на компьютере в папке программы'

def Save_as_xml():
    global names
    global phones

    book = open('my_book.xml', 'w', encoding='utf-8')
    for i in range(len(names)):
        book.write(names[i])
        book.write(' ')
        book.write(phones[i])

    return 'Файл "my_book.xml" сохранен на компьютере в папке программы'