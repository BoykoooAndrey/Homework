import input
import functions_book as fu_bo

CHOICE_ADD_CONTACT = 1
CHOICE_SEARCH = 2
CHOICE_VIEV_BOOK = 3
CHOICE_DEL_CONTACT = 4


def func():
    a = input.number_func()
    if a == CHOICE_ADD_CONTACT:
        fu_bo.rec()
    elif a == CHOICE_SEARCH:
        des_cont = str(input.search())
        fu_bo.find_cont(des_cont)
    elif a == CHOICE_VIEV_BOOK:
        fu_bo.view_conts()
    elif a == CHOICE_DEL_CONTACT:
        fu_bo.view_conts()
        temp = input.del_cont_name()
        fu_bo.del_cont(temp)
        fu_bo.view_conts()
