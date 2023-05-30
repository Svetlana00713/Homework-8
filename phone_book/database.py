import view

def add_dat(data):
    with open("db.txt", "a") as file:
        file.write(data)
    print("Новый абонент добавлен \n")
    
def search_name(name):
    with open("db.txt", "r") as file:
        data = file.readlines()
        flag = False
        for i in data:
            if name in i:
                print(i)
                flag = True
        if flag == False:
            print("Такого абонента нет \n")
            
def sort_db_name():
    with open("db.txt", "r") as file:
        data = file.readlines()
        data.sort()
    with open("db.txt", "w") as file:
        file.writelines(data)

def sort_db_date():
    with open("db.txt", "r") as file:
        data = file.readlines()
        data.sort(key=lambda x: x[4])
    with open("db.txt", "w") as file:
        file.writelines(data)
        
def print_name():
    with open("db.txt", "r") as file:
        data = file.readlines()
        for i in data:
            print(i.split(";")[0])
            
def print_db():
    with open("db.txt", "r") as file:
        print(file.read())
        
def refactor(number):
    with open("db.txt", "r") as file:
        data = file.readlines()
    new_data = view.user()
    data[number - 1] = new_data + '\n'
    with open("db.txt", "w") as file:
        file.writelines(data)

def remove(number):
    with open("db.txt", "r") as file:
        data = file.readlines()
    data[number - 1] = ''
    with open("db.txt", "w") as file:
        file.writelines(data)
 
            
            

    
            
    
    
            
                
        