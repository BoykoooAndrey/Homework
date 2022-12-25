import tkinter as tk


win = tk.Tk()

icon = tk.PhotoImage(file='img.png')
win.iconphoto(False, icon)
win.title("Телефонный справочник")
win.geometry("700x700+0+0")
win.resizable(False, False)
win.config(bg='#3D00B7')


def add_label():
    label_1 = tk.Label(win, text='Телефонный справночник',
                       bg='#3D00B7',
                       font=('Arial', 20, 'bold'),
                       pady=20,
                       )
    label_1.pack()




print(list)


btn1 = tk.Button(win, text="Добавить телефон", command=request)
btn1.pack()

win.mainloop()
