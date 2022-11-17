from tkinter import * #библиотека граф дизайна
from tkinter import ttk

import form
root = None
frm = None

def Create_menu():
    global root
    global frm
    root = Tk()
    root.title('Телефонный справочник')
    frm = ttk.Frame(root, padding=15)
    frm.grid()
    ttk.Label(frm, text='Добро пожаловать. Это ваш справочник.\n').grid(column=1, row=1)
    ttk.Button(frm, text="Вывести справочник", command=Print_phones).grid(column=0, row=7)
    ttk.Button(frm, text="Выгрузить справочник в my_book.html", command=Save_as_html).grid(column=2, row=7)
    ttk.Button(frm, text="Добавить запись(через консоль)", command=Add_phone).grid(column=0, row=8)
    ttk.Button(frm, text="Выгрузить справочник в my_book.xml", command=Save_as_xml).grid(column=2, row=8)
    ttk.Button(frm, text="Выход из справочника", command=root.destroy).grid(column=1, row=8)
    root.mainloop()


def Print_phones():
    global frm
    ttk.Label(frm, text=f'{form.Print_phones()}').grid(column=0, row=2)

def Save_as_html():
    global frm
    a = ttk.Label(frm, text=f'{form.Save_as_html()}').grid(column=0, row=3)  

def Save_as_xml():
    global frm
    a = ttk.Label(frm, text=f'{form.Save_as_xml()}').grid(column=0, row=4)  

def Add_phone():
    global frm
    ttk.Label(frm, text=f'{form.Add_phone()}').grid(column=0, row=5)  
