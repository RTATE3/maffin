



import sqlite3
import datetime
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

    frame1 = ttk.Frame(root, borderwidth=1, relief=SOLID, padding=[10, 10, 50, 10])
    frame2 = ttk.Frame(root, borderwidth=1, relief=SOLID, padding=[10, 10, 50, 10])
    frame1.pack(side="left", padx=20, pady=20)
    frame2.pack(side="left", padx=20, pady=20)

    label1 = ttk.Label(frame1, text="Введите категорию вашего расхода")
    combobox1 = ttk.Combobox(frame1, values=categories)
    def cancel_func():
        frame1.destroy()
        frame2.destroy()
        expenses_btn.config(state='enabled')
        revenues_btn.config(state='enabled')
    cancel_btn1 = ttk.Button(frame1, text="Отмена", command=cancel_func)
    label1.pack(pady=3, anchor=W)
    combobox1.pack(ipadx=40, pady=3, anchor=W)
    cancel_btn1.pack()
    combobox1.bind('<<ComboboxSelected>>', lambda event=None: save_input1())

    def save_input1():
        user_input1 = combobox1.get()
        if user_input1:
            combobox1.unbind('<Return>')
            frame1.destroy()
            print(user_input1)

            def save_input2():
                user_input2 = entry2.get()
                if user_input2:
                    print(user_input2)
                    expenses_btn.config(state='enabled')
                    revenues_btn.config(state='enabled')
                    entry2.unbind('<Return>')
                    frame2.destroy()
                else:
                    pass

            label2 = ttk.Label(frame2, text="Введите сумму")
            entry2 = ttk.Entry(frame2)
            cancel_btn2 = ttk.Button(frame2, text="Отмена", command=cancel_func)
            label2.pack(pady=3, anchor=W)
            entry2.pack(pady=3, anchor=W)
            cancel_btn2.pack()
            entry2.bind('<Return>', lambda event=None: save_input2())

def revenues_func():

    revenues_btn.config(state='disabled')
    expenses_btn.config(state='disabled')

    frame = ttk.Frame(root, borderwidth=1, relief=SOLID, padding=[10, 10, 50, 10])
    frame.pack(side="left", padx=20, pady=20)

    def cancel_func():
        frame.destroy()
        revenues_btn.config(state='enabled')
        expenses_btn.config(state='enabled')
    def save_input():
        user_input = entry.get()
        if user_input:
            print(user_input)
            revenues_btn.config(state='enabled')
            expenses_btn.config(state='enabled')
            entry.unbind('<Return>')
            frame.destroy()
        else:
            pass

    label = ttk.Label(frame, text="Введите сумму")
    entry = ttk.Entry(frame)
    cancel_btn = ttk.Button(frame, text="Отмена", command=cancel_func)
    label.pack(pady=3, anchor=W)
    entry.pack(pady=3, anchor=W)
    cancel_btn.pack()
    entry.bind('<Return>', lambda event=None: save_input())




root = Tk()
root.title('Maffin - приложение для управления личными финансами.')
root.geometry("700x200")

btn_frame = ttk.Frame(root)
btn_frame.pack(side='left', padx=20, pady=10)
expenses_btn = ttk.Button(btn_frame, text="Добавить трату", command=expenses_func)
revenues_btn = ttk.Button(btn_frame, text="Добавить доход", command=revenues_func)
expenses_btn.pack(pady=10)
revenues_btn.pack(pady=10)

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







