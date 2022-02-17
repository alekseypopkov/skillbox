# Калькулятор - версия 1
def main_menu():
   choice = input('\nВычисления - цифра 1.\nВыход - любая другая клавиша: ')
   if choice == '1':
       pass
   else:
       exit()
   operation = input('\nВыберите операцию: ')
   if (operation != '+') and (operation != '-') and (operation != '*') and (operation != '/'):
       print('\nОшибка: такой операции не существует. Попробуйте ещё раз.')
       main_menu()
   a = float(input('\nВведите первое число: '))
   b = float(input('Введите иторое число: '))
   calculator(operation, a, b)

def calculator(operation, a, b):
   #c = 0

   if operation == '+':
       c = a + b
       print(f'\n{a} + {b} =', c)
       main_menu()
   elif operation == '-':
       c = a - b
       print(f'\n{a} - {b} =', c)
       main_menu()
   elif operation == '/':
       c = a / b
       print(f'\n{a} / {b} =', c)
       main_menu()
   elif operation == '*':
       c = a * b
       print(f'\n{a} * {b} =', c)
       main_menu()
       

main_menu()