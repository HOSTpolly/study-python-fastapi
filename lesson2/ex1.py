user_1={
    'name': 'John',
    'password':'password123'
}
user_2={
    'name': 'Nik',
    'password':'pa$$w0rd123'
}

list_of_users=[user_1,user_2]

input_name = input("Введіть ваше ім'я: ")

input_password = input("Введіть ваш пароль: ")

user_found = False
for user in list_of_users:
    if user['name'] == input_name:
        user_found = True
        if user['password'] == input_password:
            print("Ви увійшли в систему")
        elif user['password'] != input_password:
            print("Неправильний пароль. Спробуйте ще раз")
            nput_password = input("Введіть ваш пароль: ")
            if user['password'] == input_password:
               print("Ви увійшли в систему")
            else: 
                print("Неправильний пароль")
        break

if not user_found:
    print("Користувача з таким ім'ям не знайдено")
