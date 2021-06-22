

todos = []


def show_todos():
    todo_index = 0
    for todo in todos:
        print(todo + " [" + str(todo_index) + "]")
        todo_index +=1

def add_todos():
    y = input("co chcesz dodać do TODO? ")
    todos.append(y)
    print ("Dodoano pomyślnie zadanie! " + y)

def del_todos():
    show_todos()
    todo_index = int (input("Podaj numer indeksu TODO, który chcesz usunąć ? "))
    if todo_index <0 or todo_index > len(todos)-1:
        print("TODO o podanym indeksie nie istnieje !")
        return
    todos.pop(todo_index)
    print("Usunięto zadanie! " + str(todo_index))
    print()

def save_todos():
    file = open("todos.txt", "w")
    for todo in todos:
        file.write(todo + "/n")
    file.close()
    print ("Zapisano TODO do pliku todos.txt")

def load(todos):
    try:
        file = open("todos.txt")
        for line in file.readlines():
            todos.append(line.strip())
        file.close()
    except FileNotFoundError:
        return
