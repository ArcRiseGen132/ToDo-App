todos = []

while True:
    user_action = input("Type add, show, edit, or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo:")
            todos.append(todo)
        case "show":
            for item in todos:
                item = item.title()
                print(item)
        case "exit":
            break
        case "edit":
            number = input("Number of the todo to edit: ")
            existing_todo = int(todos[number - 1])
            new_todo = input("Enter a new todo: ")
            todos[existing_todo] = new_todo
        case _:
            print("Unknown command entered")

print("Bye!")
