# Калькулятор - версия 2
def main_menu():
   choice = input('\nВычисления - цифра 1.\nВыход - любая другая клавиша: ')
   if choice == '1':
       pass
   else:
       exit()
   operation = input('\nВыберите операцию: ')
   lot = int(input('\nСколько операндов? '))
   if (operation != '+') and (operation != '-') and (operation != '*') and (operation != '/'):
       print('\nОшибка: такой операции не существует. Попробуйте ещё раз.')
       main_menu()
   calculator(operation, lot)

def calculator(operation, n):
   result = 0
   text = ''
   
   for number in range(1, n + 1):
       num = input(f'Введите операнд {number}: ')
       if operation == '+':
           result += float(num)
           if number == n:
               text = text + num
           else:
               text = text + num + ' + '
       if operation == '-':
           if number == n:
               text = text + num
           else:
               text = text + num + ' - '
           if number == 1:
               result = float(num)
           else:
               result -= float(num)
       if operation == '*':
           if number == 1:
               text = (f'{num}')
               result = float(num)
           else:
               text = (f'{text} * {num}')
               result *= float(num)
       if operation == '/':
           if number == 1:
               text = (f'{num}')
               result = float(num)
           else:
               text = (f'{text} / {num}') 
               result /= float(num)
   
   print(f'\n{text} =', result)
   main_menu()
       

main_menu()