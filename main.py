
from funkcje import *

# TODO

x = 0

load(todos)

while x != 5:
    if x == 1:
        show_todos()

    if x == 2:
        add_todos()

    if x == 3:
        del_todos()

    if x == 4:
        save_todos()


    print("1. Pokaż zadania TODO")
    print("2. Dodaj zadanie")
    print("3. Usuń zadanie")
    print("4. Zapisz zadania do pliku TODO.txt")
    print("5. Wyjdz")

    x = int(input("co chcesz zrobić, podaj liczę: "))
    print()
