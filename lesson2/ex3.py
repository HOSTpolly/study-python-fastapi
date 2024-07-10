print("TASK1. Таблиця множення\nЗавдання: Виведіть таблицю множення для заданого числа від 1 до 10.")
a=0
for a in range(10):
    a+=1
    b=5
    b=b*a
    print(b)
    
print("\nTASK2. Сума чисел\nЗавдання: Визначте список чисел і обчисліть їх суму")
import random

random_list = [random.randint(1, 20) for _ in range(10)]
print("Random List:", random_list)
sum=0
for num in random_list:
    sum+=num
print("cума чисел:",sum)



print("\nTASK3. Факторіал числа\nЗавдання: Обчисліть факторіал заданого числа.")
a=6
def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
        
print(fact(a))

print("\nTASK4. Hепарні числа\nЗавдання: Виведіть всі парні числа від 1 до 50")

array_neparni=[]
array_parni=[]
for i in range(1, 50):
    if i%2:
        array_neparni.append(i)
    else:
        array_parni.append(i)
print(array_parni)

print("\nTASK5. Пошук простих чисел\nЗавдання: Знайдіть всі прості числа в заданому діапазоні.")


prosty=[]
start = 2
end = 1000
numbers = list(range(start, end))

current_num = start

# while current_num < end:
#     # Check if the number is not divisible by 2
#      if current_num % 2 != 0   or current_num == 2:
#         # Check if the number is not divisible by 3
#         if current_num % 3 != 0   or current_num == 3 :
#             if current_num % 5 != 0  or current_num == 5 :
#                 if current_num % 7!=0 or current_num == 7 :
            
#                      prosty.append(current_num)
            
#      current_num += 1


for current_num in numbers:
    is_proste = True
    for i in range(2, int(current_num ** 0.5) + 1):
        if current_num % i == 0:
            is_proste = False
            break
    if is_proste:
        prosty.append(current_num) 
                

print(prosty)   
    