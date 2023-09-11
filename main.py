



import sqlite3
import datetime
import time
from tkinter import *
from tkinter import ttk

categories = [
    'Продукты питания и рестораны',
    'Жилье и коммунальные услуги',
    'Транспорт',
    'Здоровье и медицина',
    'Образование',
    'Развлечения и хобби',
    'Личные расходы',
    'Финансовые услуги',
    'Домашние расходы',
    'Дети и семья'
]

def expenses_func():
    expenses_btn.config(state='disabled')
    revenues_btn.config(state='disabled')
    frame = ttk.Frame(root)
    frame1 = ttk.Frame(root)
    frame2 = ttk.Frame(root)
    frame1.pack(anchor=N, side="left", padx=20, pady=20)
    frame2.pack(anchor=N, side="left", padx=20, pady=20)
    frame.pack(anchor=N, side="left", padx=20, pady=40)

    label1 = ttk.Label(frame1, text="Введите категорию вашего расхода")
    combobox = ttk.Combobox(frame1, values=categories)

    def cancel_func():
        frame.destroy()
        frame1.destroy()
        frame2.destroy()
        expenses_btn.config(state='enabled')
        revenues_btn.config(state='enabled')

    cancel_btn1 = ttk.Button(frame1, text="Отмена", command=cancel_func)
    label1.pack(pady=3, anchor=W)
    combobox.pack(ipadx=40, pady=3, anchor=W)
    cancel_btn1.pack(pady=2)
    combobox.bind('<<ComboboxSelected>>', lambda event=None: input_categoria())

    def input_categoria():
        categoria = combobox.get()
        if categoria:
            combobox.unbind('<Return>')
            frame1.destroy()
            categoria_label = ttk.Label(frame, text=f'Категория:      {categoria}')
            categoria_label.pack()

            def input_summ():
                summ = entry2.get()
                if summ:
                    summ_label = ttk.Label(frame, text=f'Сумма:         {summ} руб.')
                    summ_label.pack()
                    expenses_btn.config(state='enabled')
                    revenues_btn.config(state='enabled')
                    entry2.unbind('<Return>')
                    frame2.destroy()
                    root.after(5000, frame.destroy)

            input_summ_label = ttk.Label(frame2, text="Введите сумму")
            entry2 = ttk.Entry(frame2)
            cancel_btn2 = ttk.Button(frame2, text="Отмена", command=cancel_func)
            input_summ_label.pack(pady=3, anchor=W)
            entry2.pack(pady=3, anchor=W)
            cancel_btn2.pack(pady=2)
            entry2.bind('<Return>', lambda event=None: input_summ())

def revenues_func():
    revenues_btn.config(state='disabled')
    expenses_btn.config(state='disabled')

    frame = ttk.Frame(root)
    frame.pack(anchor=N, side="left", padx=20, pady=20)
    frame1 = ttk.Frame(root)
    frame1.pack(anchor=N, side="left", padx=20, pady=40)

    def cancel_func():
        frame.destroy()
        frame1.destroy()
        revenues_btn.config(state='enabled')
        expenses_btn.config(state='enabled')
    def save_input():
        user_input = input_summ_entry.get()
        if user_input:
            summ_label = ttk.Label(frame1, text=f'{user_input} руб.')
            summ_label.pack()
            revenues_btn.config(state='enabled')
            expenses_btn.config(state='enabled')
            input_summ_entry.unbind('<Return>')
            frame.destroy()
            root.after(5000, frame1.destroy)

    input_summ_label = ttk.Label(frame, text="Введите сумму")
    input_summ_entry = ttk.Entry(frame)
    cancel_btn = ttk.Button(frame, text="Отмена", command=cancel_func)
    input_summ_label.pack(pady=3, anchor=W)
    input_summ_entry.pack(pady=3, anchor=W)
    cancel_btn.pack(pady=2)
    input_summ_entry.bind('<Return>', lambda event=None: save_input())

root = Tk()
root.title('Maffin - приложение для управления личными финансами.')
root.geometry("700x500")

btn_frame = ttk.Frame(root)
btn_frame.pack(side='left', anchor=N, padx=20, pady=10)
expenses_btn = ttk.Button(btn_frame, text="Добавить трату", command=expenses_func)
revenues_btn = ttk.Button(btn_frame, text="Добавить доход", command=revenues_func)
expenses_btn.pack(anchor=NW, pady=10, padx=10)
revenues_btn.pack(anchor=NW, pady=10, padx=10)

languages_var = Variable(value=categories)
languages_listbox = Listbox(btn_frame, listvariable=languages_var)
languages_listbox.pack(anchor=NW, ipady=80, ipadx=80, pady=20, padx=10)

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







