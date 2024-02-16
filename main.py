import addItems, deleteitems, readitems, updateitems, search

def read_file():
    try:
        with open("mainMenu.txt") as readFile:
            rf = readFile.read()
        return rf
    except FileNotFoundError as notFound:
        print(f"Check {notFound}")

def filmflix_menu():
    option = 0
    options = ["1", "2", "3", "4", "5",]
    
    menu = read_file()

    while option not in options:
        print(menu)

        option = input("Enter an option from the above choices: ")

        if option not in options:
            print(f"{option} is not a valid choice.")
    return option

program = True

while program:
    main = filmflix_menu()
    
    match main:
        case "1":
            readitems.read_items()
        case "2":
            addItems.insert_data()
        case "3":
            updateitems.update_items()
        case "4":
            deleteitems.delete_items()
        case "5":
            search.search_data()
        case _:
            program = False
input("Press Enter key to exit: ")
                