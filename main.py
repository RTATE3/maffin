



import sqlite3
import datetime
from tkinter import *
from tkinter import ttk


def expenses_func():
    btn.config(state='disabled')
    label.config(text='Введите сумму')


def revenues_func():
    btn1.config(state='disabled')


root = Tk()
root.title('Maffin - приложение для управления личными финансами.')
root.geometry("500x600")

btn = ttk.Button(text="Добавить трату", command=expenses_func)
btn1 = ttk.Button(text="Добавить доход", command=revenues_func)
btn.pack(ipady=20)
btn1.pack(ipady=18)

label = ttk.Label(text="")
label.pack(anchor=CENTER, expand=True)
ttk.Entry().pack(anchor=N, padx=8, pady=8)




root.mainloop()

# transaction = int(input('Доходы или расходы? 1/0'))
# current_date = str(datetime.datetime.now())
#
# with sqlite3.connect('maffin.db') as connection:
#     cursor = connection.cursor()
#     if transaction:
#         revenues = int(input('Сколько?'))
#         cursor.execute('INSERT INTO FinTransaction (date, summ, categoria) VALUES (?, ?, ?)',
#                        (current_date, revenues, 'Доход'))
#
#     else:
#         categoria = input('Введите категорию вашего расхода: ')
#         summ = int(input('Введите сумму вашего расхода: '))
#         cursor.execute('INSERT INTO FinTransaction (date, summ, categoria) VALUES (?, ?, ?)',
#                        (current_date, summ, categoria))







