firm_data = {}

def add_employee():
    name = input("Введите ФИО: ")
    phone = input("Введите телефон: ")
    email = input("Введите рабочий email: ")
    position = input("Введите должность: ")
    office = input("Введите номер кабинета: ")
    skype = input("Введите Skype: ")

    employee = {
        "ФИО": name,
        "Телефон": phone,
        "Email": email,
        "Должность": position,
        "Кабинет": office,
        "Skype": skype
    }

    firm_data[name] = employee
    print("Сотрудник успешно добавлен.")

def delete_employee():
    name = input("Введите ФИО сотрудника, которого нужно удалить: ")
    if name in firm_data:
        del firm_data[name]
        print("Сотрудник успешно удален.")
    else:
        print("Сотрудник не найден.")

def search_employee():
    name = input("Введите ФИО сотрудника, которого нужно найти: ")
    if name in firm_data:
        employee = firm_data[name]
        print("Информация о сотруднике:")
        print("ФИО:", employee["ФИО"])
        print("Телефон:", employee["Телефон"])
        print("Email:", employee["Email"])
        print("Должность:", employee["Должность"])
        print("Кабинет:", employee["Кабинет"])
        print("Skype:", employee["Skype"])
    else:
        print("Сотрудник не найден.")

def update_employee():
    name = input("Введите ФИО сотрудника, которого нужно обновить: ")
    if name in firm_data:
        employee = firm_data[name]
        new_phone = input("Введите новый телефон (или нажмите Enter, чтобы оставить без изменений): ")
        if new_phone:
            employee["Телефон"] = new_phone
        new_email = input("Введите новый email (или нажмите Enter, чтобы оставить без изменений): ")
        if new_email:
            employee["Email"] = new_email
        new_position = input("Введите новую должность (или нажмите Enter, чтобы оставить без изменений): ")
        if new_position:
            employee["Должность"] = new_position
        new_office = input("Введите новый номер кабинета (или нажмите Enter, чтобы оставить без изменений): ")
        if new_office:
            employee["Кабинет"] = new_office
        new_skype = input("Введите новый Skype (или нажмите Enter, чтобы оставить без изменений): ")
        if new_skype:
            employee["Skype"] = new_skype
        firm_data[name] = employee
        print("Информация о сотруднике обновлена.")
    else:
        print("Сотрудник не найден.")

while True:
    print("\nВыберите действие:")
    print("1. Добавить сотрудника")
    print("2. Удалить сотрудника")
    print("3. Найти сотрудника")
    print("4. Обновить информацию о сотруднике")
    print("5. Выход")

    choice = input("Введите номер действия: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        delete_employee()
    elif choice == "3":
        search_employee()
    elif choice == "4":
        update_employee()
    elif choice == "5":
        print("Выход из программы.")
        break
    else:
        print("Неверный выбор. Попробуйте еще раз.")
