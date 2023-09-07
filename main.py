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
import datetime
transaction = input('Доходы или расходы? 1/0')
current_date = datetime.datetime.now()


class Expenses:

    def __init__(self, categoria, summ):
        self.categoria = categoria
        self.summ = summ


with sqlite3.connect('maffin.db') as connection:
    cursor = connection.cursor()
    if int(transaction):
        revenues = input('Сколько?')
        cursor.execute('INSERT INTO FinTransaction (date, summ, categoria) VALUES (?, ?, ?)',
                       (str(current_date), int(revenues), 'Доход'))

    else:
        expenses = Expenses(categoria=input('Введите категорию вашего расхода: '),
                            summ=input('Введите сумму вашего расхода: '))
        print(expenses.categoria)
        print(expenses.summ)
        # cursor.execute('INSERT INTO








