#Завдання: Створіть програму, яка встановлює номер дня тижня і виводить назву відповідного дня тижня. 
# Якщо номер дня недійсний (менше 1 або більше 7), виведіть повідомлення про помилку.

day_1={
    'name': 'Monday',
    'num':'1'
}
day_2={
    'name': 'Tuesday',
    'num':'2'
}
day_3={
    'name': 'Wednesday',
    'num':'3'
}
day_4={
    'name': 'Thursday',
    'num':'4'
}
day_5={
    'name': 'Friday',
    'num':'5'
}
day_6={
    'name': 'Saturday',
    'num':'6'
}
day_7={
    'name': 'Sunday',
    'num':'7'
}


list_of_days = [day_1,day_2,day_3,day_4,day_5,day_6,day_7]


day_found = False
input_num = input("Введіть номер дня тижня: ")

if int(input_num) <= -1 :
    print("Mistake\nВи вели номер дня тижня менше 1")
elif int(input_num) > 7:
    print("Mistake\nВи вели номер дня тижня більший за 7")
else:
    for day in list_of_days:
     if day['num'] == input_num:
        day_found = True
        print("Correct\n",day['name'])
        break