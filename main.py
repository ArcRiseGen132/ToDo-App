todos = []

while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo:")
            todos.append(todo)
        case "show":
            for index, item in enumerate(todos):
                row = f"{int(index) + 1}--{item.title()}"  # Add 1 to make numbering user-friendly
                print(row)
        case "exit":
            break
        case "edit":
            number = input("Number of the todo to edit: ")
            existing_todo = int(todos[int(number) - 1])  # Subtract 1 for true array placement
            new_todo = input("Enter a new todo: ")
            todos[existing_todo] = new_todo
        case "complete":
            number = int(input("Number of the todo to complete or remove: "))
            todos.pop(number - 1)  # Subtract 1 to find actual array placement
        case _:
            print("Unknown command entered")

print("Bye!")
