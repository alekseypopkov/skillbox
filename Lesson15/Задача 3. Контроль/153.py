id_office = []
id_count = int(input('Кол-во сотрудников в офисе: '))
for id in range(1,id_count + 1):
    id = int(input(f'ID сотрудника {id}: '))
    id_office.append(id)
while True:
    id_choce = int(input('Какой ID ищем? '))
    if id_choce in id_office:
        print('Сотрудник на месте')
    else:
        print('Сотрудник не работает!')