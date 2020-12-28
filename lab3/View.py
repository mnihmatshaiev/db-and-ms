def menu_task1_create():
    print(" Choose table:\n Film - press 1\n Hall - press 2\n Show - press 3\n Ticket - press 4")
    table = int(input())
    param1 = None
    param2 = None
    param3 = None
    if table == 1:
        print(" Enter film name")
        param1 = input()
    elif table == 2:
        print(" Enter hall name")
        param1 = input()
        print(" Enter capacity")
        param2 = int(input())
    elif table == 3:
        print(" Enter film id")
        param2 = int(input())
        print(" Enter hall id")
        param1 = int(input())
        print(" Enter start date")
        param3 = input()
    elif table == 4:
        print(" Enter show id")
        param1 = int(input())
        print(" Enter row")
        param2 = int(input())
        print(" Enter seat")
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
        print(" Enter the id of the film you want to delete")
        parameter1 = int(input())
    elif table == 2:
        print(" Enter the id of the hall you want to delete")
        parameter1 = int(input())
    elif table == 3:
        print(" Enter the id of the show you want to delete")
        parameter1 = int(input())
    elif table == 4:
        print(" Enter the id of the show, row and set you want to delete")
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
        print(" Enter film name")
        param1 = input()
        print("Enter the id of the film you want to edit")
        param2 = int(input())
    elif table == 2:
        print("Enter hall name")
        param1 = input()
        print(" Enter capacity")
        param2 = int(input())
        print("Enter the id of the hall you want to edit")
        param3 = int(input())
    elif table == 3:
        print(" Enter film id")
        param2 = int(input())
        print(" Enter hall id")
        param1 = int(input())
        print(" Enter start date")
        param3 = input()
        print("Enter the id of the show you want to edit")
        param4 = int(input())
    elif table == 4:
        print(" Enter row\n")
        param1 = int(input())
        print(" Enter seat\n")
        param2 = int(input())
        print("Enter the id of the show you want to edit")
        param3 = int(input())
        print("Enter the row you want to edit")
        param4 = int(input())
        print("Enter the seat you want to edit")
        param5 = int(input())
    else:
        print("False number")
        return
    return table, param1, param2, param3, param4, param5


def menu_task_1_print():
    print(" Choose table: Film - press 1 Hall - press 2 Show - press 3 Ticket - press 4")
    table = int(input())
    return table



