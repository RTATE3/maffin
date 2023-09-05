# from tkinter import *
# from tkinter import ttk
#
#
# root = Tk()
# root.title('Maffin')
# frm = ttk.Frame(root, padding=100)
# frm.grid()
# ttk.Label(frm, text="""Приложение для управления личными финансами""").grid(column=0, row=0)
# ttk.Button(frm, text="Закрыть", command=root.destroy).grid(column=0, row=5)
# root.mainloop()

import sqlite3
transaction = input('Доходы или расходы? 1/0')


class Expenses:

    def __init__(self, categoria, summ):
        self.categoria = categoria
        self.summ = summ

with sqlite3.connect('maffin') as connection:
    cursor = connection.cursor()
    if int(transaction):
        revenues = input('Сколько?')
        print(revenues)
        cursor.execute('INSERT INTO
    else:
        expenses = Expenses(categoria=input('Введите категорию вашего расхода: '),
                            summ=input('Введите сумму вашего расхода: '))
        print(expenses.categoria)
        print(expenses.summ)
        cursor.execute('INSERT INTO








