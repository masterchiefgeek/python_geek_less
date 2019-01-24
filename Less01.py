print('Добро пожаловать в вашу медецинскую анкету. Мы зададим Вам пару вопросов')
name = input('Ваше имя: ')
surname = input('Ваша фамилия: ')
age = int(input('Ваш возраст (полных лет): '))
weight = int(input('Ваш вес: '))
if age < 30 and 120 > weight >= 50:
    print(name, surname + ', полных лет', age, 'вес', weight, '- состояние вашего здоровья хорошее.')
elif 100 <= age >= 30 and 120 > weight >= 50: # В задании не предусмотрели что здоровые могут быть и после 30 :)
    print(name, surname + ', полных лет', age, 'вес', weight, '- состояние вашего здоровья хорошее.')
elif 40 >= age >= 30 and ((weight < 50 and weight > 40) or (weight >= 120 and weight < 140)):
    print(name, surname + ', полных лет', age, 'вес', weight,
          '- Вам следует заняться собой и вести правильный образ жизни')  # PEP-8 рекомендует сокращать строки до 120 символов, не критично, но на моем маленьком экране реально легче
elif 40 >= age >= 30 and (weight < 40 or weight >= 140):
    print(name, surname + ', полных лет', age, 'вес', weight, '- Вам требуется немедленный врачебный осмотр')
elif 41 >= age <= 100 and ((weight < 50 and weight > 40) or (weight >= 120 and weight < 140)):
    print(name, surname + ', полных лет', age, 'вес', weight, '- Вам требуется врачебный осмотр')
elif 41 >= age and (weight < 40 or weight >= 140):
    print(name, surname + ', полных лет', age, 'вес', weight, '- Вам требуется немедленный врачебный осмотр')
elif age >= 101 and 120 >= weight >= 50:
    print(name, surname + ', полных лет', age, 'вес', weight, '- Мы Вам завидуем!')
elif age >= 101 and (weight < 40 or weight >= 140):
    print(name, surname + ', полных лет', age, 'вес', weight, '- Ээээм...')
