import view
import database

def main():
    while True:
        choice = view.user_input()
        print(choice)
        if choice == 1:
            data = view.user()
            database.add_dat(data)
        elif choice == 2:
            name = view.search()
            database.search_name(name)
        elif choice == 3:
            database.sort_db_name()
        elif choice == 4:
            database.sort_db_date()  
        elif choice == 5:
            database.print_name()
        elif choice == 6:
            database.print_db() 
        elif choice == 7:
            print(database.print_name())
            database.refactor(int(input('Введите номер изменения: ')))   
        elif choice == 8:
            database.remove(int(input('Введите номер удаления: ')))
        elif choice == 9:
            break
        
main()
    