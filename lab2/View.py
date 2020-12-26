def menu_task1_create():
    print(" Choose table:\n Film - press 1\n Hall - press 2\n Show - press 3\n Ticket - press 4")
    table = int(input())
    param1 = None
    param2 = None
    param3 = None
    if table == 1:
        print(" Enter film name\n")
        param1 = input()
    elif table == 2:
        print(" Enter hall name\n")
        param1 = input()
        print(" Enter capacity\n")
        param2 = int(input())
    elif table == 3:
        print(" Enter film id\n")
        param1 = int(input())
        print(" Enter hall id\n")
        param2 = int(input())
        print(" Enter start date\n")
        param3 = input()
    elif table == 4:
        print(" Enter show id\n")
        param1 = int(input())
        print(" Enter row\n")
        param2 = int(input())
        print(" Enter seat\n")
        param3 = int(input())
    else:
        print(" False number")
        return
    return table, param1, param2, param3


def menu_task_1_delete():
    print(" Choose table:\n Film - press 1\n Hall - press 2\n Show - press 3\n Ticket - press 4")
    table = int(input())
    (parameter1, parameter2, parameter3) = (None, None, None)
    if table == 1:
        print(" Enter the id of the film you want to delete\n")
        parameter1 = int(input())
    elif table == 2:
        print(" Enter the id of the hall you want to delete\n")
        parameter1 = int(input())
    elif table == 3:
        print(" Enter the id of the show you want to delete\n")
        parameter1 = int(input())
    elif table == 4:
        print(" Enter the id of the show, row and set you want to delete\n")
        parameter1 = int(input())
        parameter2 = int(input())
        parameter3 = int(input())
    else:
        print(" False number")
        return
    return table, parameter1, parameter2, parameter3


def menu_task_1_edit():
    print(" Choose table:\n Film - press 1\n Hall - press 2\n Show - press 3\n Ticket - press 4")
    table = int(input())
    (param1, param2, param3, param4, param5) = (None, None, None, None, None)
    if table == 1:
        print(" Enter film name\n")
        param1 = input()
        print("Enter the id of the film you want to edit\n")
        param2 = int(input())
    elif table == 2:
        print("Enter hall name\n")
        param1 = input()
        print(" Enter capacity\n")
        param2 = int(input())
        print("Enter the id of the hall you want to edit\n")
        param3 = int(input())
    elif table == 3:
        print(" Enter film id\n")
        param1 = int(input())
        print(" Enter hall id\n")
        param2 = int(input())
        print(" Enter start date\n")
        param3 = input()
        print("Enter the id of the show you want to edit\n")
        param4 = int(input())
    elif table == 4:
        print(" Enter row\n")
        param1 = int(input())
        print(" Enter seat\n")
        param2 = int(input())
        print("Enter the id of the show you want to edit\n")
        param3 = int(input())
        print("Enter the row you want to edit\n")
        param4 = int(input())
        print("Enter the seat you want to edit\n")
        param5 = int(input())
    else:
        print("False number")
        return
    return table, param1, param2, param3, param4, param5


def menu_task_1_print():
    print(" Enter table: film, hall, show or ticket")
    table = input()
    return table


def menu_task_2():
    print(" Choose table:\n Film - press 1\n Hall - press 2\n Show - press 3\n Ticket - press 4")
    table = int(input())
    number = None
    if table == 1 or table == 2:
        print(" Input number of lines in tables")
        number = int(input())
    return table, number


def menu_task_3():
    print(" Enter: 1, 2 or 3 for testing select")
    item_3 = int(input())
    if item_3 == 1:
        print(" Enter the name of the film to find out in which name hall it is taking place")
    elif item_3 == 2:
        print(" Enter film id to find out the number of free seats for it")
    elif item_3 == 3:
        print(" Enter the id of the show to find out the capacity of the hall in which it takes place")
    else:
        print("False number")
        return
    param = input()
    return param, item_3
