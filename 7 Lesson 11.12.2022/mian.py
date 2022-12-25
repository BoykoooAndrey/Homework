import tkinter as tk
import csv
import functions_book as fu_bo


# Убрать меню и вернуть меню
def remove_menu():
    btn_add_cont.place_forget()
    btn_view_book.place_forget()
    btn_del_menu.place_forget()
    btn_search_cont.place_forget()


def return_menu():
    btn_add_cont.place(relwidth=0.25, relheight=1, relx=0, rely=0)
    btn_view_book.place(relwidth=0.25, relheight=1, relx=0.25, rely=0)
    btn_del_menu.place(relwidth=0.25, relheight=1, relx=0.5, rely=0)
    btn_search_cont.place(relwidth=0.25, relheight=1, relx=0.75, rely=0)
# Вызов функции "Добавить контакт"


def put_entry():
    def put_widget_entry():
        label_name.place(relwidth=0.5, relheight=0.05, relx=0, rely=0.1)
        label_surname.place(relwidth=0.5, relheight=0.05, relx=0, rely=0.15)
        label_number.place(relwidth=0.5, relheight=0.05, relx=0, rely=0.2)
        label_note.place(relwidth=0.5, relheight=0.05, relx=0, rely=0.25)
        name.place(relwidth=0.5, relheight=0.05, relx=0.5, rely=0.1)
        surname.place(relwidth=0.5, relheight=0.05, relx=0.5, rely=0.15)
        number.place(relwidth=0.5, relheight=0.05, relx=0.5, rely=0.2)
        note.place(relwidth=0.5, relheight=0.05, relx=0.5, rely=0.25)
        btn_save_entry.place(relwidth=0.5, relheight=1, relx=0, rely=0)
        btn_exit_fentry.place(relwidth=0.5, relheight=1, relx=0.5, rely=0)
        remove_menu()
    put_widget_entry()

# Сохранение введенных данных по кнопке Save


def get_entry():
    list = []

    def append_in_list():
        list.append(name.get())
        list.append(surname.get())
        list.append(number.get())
        list.append(note.get())
    append_in_list()
    with open("tel_dir.csv", 'a', newline='') as f:
        csv.writer(f).writerow(list)

    def clear_entry():
        name.delete(0, tk.END)
        surname.delete(0, tk.END)
        number.delete(0, tk.END)
        note.delete(0, tk.END)
    clear_entry()

# Выход из функции "Добавить контакт" по кнопке Back


def exit_from_entry():
    def del_entry():
        name.place_forget()
        surname.place_forget()
        number.place_forget()
        note.place_forget()
        btn_save_entry.place_forget()
        btn_exit_fentry.place_forget()
        label_name.place_forget()
        label_surname.place_forget()
        label_number.place_forget()
        label_note.place_forget()
        return_menu()
    del_entry()

    def clear_entry():
        name.delete(0, tk.END)
        surname.delete(0, tk.END)
        number.delete(0, tk.END)
        note.delete(0, tk.END)
    clear_entry()


# Функция вывода контактов


def view_conts():
    list = fu_bo.view_conts()
    for i in range(len(list)+1):
        for j in range(len(list[0])+1):
            if j == 0 and i == 0:
                label_i_j = tk.Label(frame_working_area, text='id',
                                     bg='#3D00B7',
                                     font=('Arial', 10),
                                     pady=1,
                                     )
                label_i_j.place(relwidth=0.2, relheight=0.04,
                                relx=0, rely=0+(i*0.04))
            elif i == len(list):
                break
            elif j == 0:
                list_id.append(str(i))
                label_i_j = tk.Label(frame_working_area, text=f'{i}',
                                     bg='#3D00B7',
                                     font=('Arial', 10),
                                     pady=1,
                                     )
                label_i_j.place(relwidth=0.2, relheight=0.04,
                                relx=0, rely=0+(i*0.04))
            else:
                label_i_j = tk.Label(frame_working_area, text=f'{((list[i])[j-1])}',
                                     bg='#3D00B7',
                                     font=('Arial', 10),
                                     pady=1,
                                     )
                label_i_j.place(relwidth=0.2, relheight=0.04,
                                relx=0+(j*0.2), rely=0+(i*0.04))

# Функция представления телефонного справочника


def view_book():
    remove_menu()
    btn_exit_fviev.place(relwidth=1, relheight=1, relx=0, rely=0)
    view_conts()

# Функция выхода из View book, Del, Find


def exit_from_view_del_find():
    def del_view():
        for widgets in frame_working_area.winfo_children():
            widgets.place_forget()
        for widgets in frame_navigation.winfo_children():
            widgets.place_forget()
    del_view()
    return_menu()


# Функция вызова меню удаления
def menu_del():
    remove_menu()
    view_conts()
    label_del.place(relwidth=0.25, relheight=1, relx=0, rely=0)
    del_id.place(relwidth=0.25, relheight=1, relx=0.25, rely=0)
    btn_del_cont.place(relwidth=0.25, relheight=1, relx=0.5, rely=0)
    btn_exit_fdel.place(relwidth=0.25, relheight=1, relx=0.75, rely=0)
# Функция удаления контакта


def del_cont():
    temp = del_id.get()
    del_id.delete(0, tk.END)
    if temp in list_id and len(temp) == 1:
        fu_bo.del_cont(int(temp)-1)
    list_id.clear()
    for widgets in frame_working_area.winfo_children():
        widgets.place_forget()
    view_conts()


# Функция вызова меню поиска
def menu_find():
    remove_menu()
    label_find.place(relwidth=0.25, relheight=1, relx=0, rely=0)
    find_request.place(relwidth=0.25, relheight=1, relx=0.25, rely=0)
    btn_find_cont.place(relwidth=0.25, relheight=1, relx=0.5, rely=0)
    btn_exit_ffind.place(relwidth=0.25, relheight=1, relx=0.75, rely=0)

# Функция поиска контакта
def search_cont():
    def del_working_area():
        for widgets in frame_working_area.winfo_children():
            widgets.place_forget()
    del_working_area()
    temp = find_request.get()
    find_request.delete(0, tk.END)
    list = fu_bo.find_cont(temp)
    for i in range(len(list)+1):
        for j in range(len(list[0])+1):
            if j == 0 and i == 0:
                label_i_j = tk.Label(frame_working_area, text='id',
                                     bg='#3D00B7',
                                     font=('Arial', 10),
                                     pady=1,
                                     )
                label_i_j.place(relwidth=0.2, relheight=0.04,
                                relx=0, rely=0+(i*0.04))
            elif i == len(list):
                break
            elif j == 0:
                label_i_j = tk.Label(frame_working_area, text=f'{i}',
                                     bg='#3D00B7',
                                     font=('Arial', 10),
                                     pady=1,
                                     )
                label_i_j.place(relwidth=0.2, relheight=0.04,
                                relx=0, rely=0+(i*0.04))
            else:
                label_i_j = tk.Label(frame_working_area, text=f'{((list[i])[j-1])}',
                                     bg='#3D00B7',
                                     font=('Arial', 10),
                                     pady=1,
                                     )
                label_i_j.place(relwidth=0.2, relheight=0.04,
                                relx=0+(j*0.2), rely=0+(i*0.04))


# Создание окна
win = tk.Tk()
icon = tk.PhotoImage(file='img.png')
win.iconphoto(False, icon)
win.title("Телефонный справочник")
win.geometry("700x700+0+0")
win.resizable(False, False)
win.config(bg='#3D00B7')


# Frame's
frame_top = tk.Frame(win, bg='#3D00B7')
frame_top.place(relwidth=1, relheight=0.1, relx=0, rely=0)
frame_navigation = tk.Frame(win,  bg='#3D00B7')
frame_navigation.place(relwidth=1, relheight=0.05, relx=0, rely=0.1)
frame_working_area = tk.Frame(win, bg='#3D00B7')
frame_working_area.place(relwidth=1, relheight=0.85, relx=0, rely=0.15)
# Labels


def labels():
    global label_1
    label_1 = tk.Label(frame_top, text='Телефонный справночник',
                       bg='#3D00B7',
                       font=('Arial', 20, 'bold'),
                       pady=20,
                       )
    label_1.pack()

    global label_name
    label_name = tk.Label(frame_working_area, text='Name',
                          bg='#3D00B7',
                          font=('Arial', 10, 'bold'),
                          )
    global label_surname
    label_surname = tk.Label(frame_working_area, text='Surname',
                             bg='#3D00B7',
                             font=('Arial', 10, 'bold'),
                             )
    global label_number
    label_number = tk.Label(frame_working_area, text='Number',
                            bg='#3D00B7',
                            font=('Arial', 10, 'bold'),
                            )
    global label_note
    label_note = tk.Label(frame_working_area, text='Note',
                          bg='#3D00B7',
                          font=('Arial', 10, 'bold'),
                          )
    global label_del
    label_del = tk.Label(frame_navigation, text='Введите id контакта',
                         bg='#3D00B7',
                         font=('Arial', 10, 'bold'),
                         )
    global label_find
    label_find = tk.Label(frame_navigation, text='Введите посковый запрос',
                         bg='#3D00B7',
                         font=('Arial', 10, 'bold'),
                         )


labels()

# Entry's
name = tk.Entry(frame_working_area)
surname = tk.Entry(frame_working_area)
number = tk.Entry(frame_working_area)
note = tk.Entry(frame_working_area)
del_id = tk.Entry(frame_navigation)
find_request = tk.Entry(frame_navigation)

# Button's
btn_add_cont = tk.Button(
    frame_navigation, text="Add contact", command=put_entry)
btn_save_entry = tk.Button(frame_navigation, text="Save", command=get_entry)
btn_exit_fentry = tk.Button(
    frame_navigation, text="Back", command=exit_from_entry)
#
btn_view_book = tk.Button(
    frame_navigation, text="View contact's", command=view_book)
btn_exit_fviev = tk.Button(
    frame_navigation, text="Back", command=exit_from_view_del_find)
#
btn_del_menu = tk.Button(
    frame_navigation, text="Delet contact", command=menu_del)
btn_del_cont = tk.Button(
    frame_navigation, text="Delet", command=del_cont)
btn_exit_fdel = tk.Button(
    frame_navigation, text="Back", command=exit_from_view_del_find)
#
btn_search_cont = tk.Button(
    frame_navigation, text="Find contact", command=menu_find)
btn_find_cont = tk.Button(
    frame_navigation, text="Search", command=search_cont)
btn_exit_ffind = tk.Button(
    frame_navigation, text="Back", command=exit_from_view_del_find)

list_id = []
return_menu()
win.mainloop()
