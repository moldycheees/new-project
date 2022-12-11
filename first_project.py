print('Приложение MyProfile\n'
      'Сохраняй информацию о себе и выводи её в разных форматах')

SEPARATOR = '\n------------------------------------------\n'

#arguments
name, age, phone_number, email_address, index, address, additional_info,OGRNIP, INN, settlement_account, bank_of_beneficiary, BIK, correspondent_account = '', '', '', '', '', '', '', '', '', '', '', '', ''

#--------------------------------------------------------------

def personal_info(
  name, age, phone_number, email_address,
  index, address, additional_info):

  name = input('\nВведите имя: ')
  age = int(input('Введите возраст: '))
  while age <= 0:
    print('Ошибка ввода.')
    age = int(input('Введите возраст: '))
  phone_number = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
  possible_sym = '0123456789+'
  for symbol in phone_number:
    if symbol not in possible_sym:  
      print('Ошибка ввода.')
      phone_number = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
  while len(str(phone_number)) != 12:
    print('Ошибка ввода.')
    phone_number = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
  email_address = input('Введите адрес электронной почты: ')
  postcode = input('Введите почтовый индекс: ')
  possible_sym = '0123456789'
  index = ''
  for symbol in postcode:
    if symbol in possible_sym:
      index += symbol
  address = input('Введите почтовый адресс (без индекса): ')
  additional_info = input('Введите дополнительную информацию: ')
  
  return name, age, phone_number, email_address, int(index), address, additional_info

#-------------------------------------------------------------- 
  
def entrepreneur_info(
  OGRNIP, INN, settlement_account, 
  bank_of_beneficiary, BIK, correspondent_account):

  OGRNIP = int(input('Введите ОГРНИП: '))
  while len(str(OGRNIP)) != 15:
    print('ОГРНИП должен содерать 15 цифр')
    OGRNIP = int(input('Введите ОГРНИП: '))
  
  INN = int(input('Введите ИНН: '))
  settlement_account = int(input('Введите расчетный счет: '))
  while len(str(settlement_account)) != 20:
    print('расчетный счет должен содерать 20 цифр')
    settlement_account = int(input('Введите расчетный счет: '))
    
  bank_of_beneficiary = input('Введите название банка: ')
  BIK = int(input('Введите БИК: ' ))
  correspondent_account = int(input('Введите корреспондентский счет: '))
  
  return OGRNIP, INN, settlement_account, bank_of_beneficiary, BIK, correspondent_account

#--------------------------------------------------------------

while True: #main_menu
  print(SEPARATOR)
  print('ГЛАВНОЕ МЕНЮ')
  main_choice = int(input('\n1 - Ввести или обновить информацию\n'
                          '2 - Вывести информацию\n' 
                          '0 - Завершить работу\n'
                          'Введите номер пункта меню: '
                          ))
  if main_choice == 1: #submenu_1
    while True:
      print(SEPARATOR)
      print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
      sub_choice = int(input('\n1 - Личная информация\n'
                             '2 - Информация о предпринимателе\n' 
                             '0 - Назад\n'
                             'Введите номер пункта меню: '
                             ))
      if sub_choice == 1:
        name, age, phone_number, email_address, index, address, additional_info = personal_info(name, age, phone_number, email_address, index, address, additional_info)
  
      elif sub_choice == 2:
        OGRNIP, INN, settlement_account, bank_of_beneficiary, BIK, correspondent_account = entrepreneur_info(OGRNIP, INN, settlement_account, bank_of_beneficiary, BIK, correspondent_account)

      elif sub_choice == 0:
        break

      else:
        print('Введён некорректный пункт меню.')
    
  elif main_choice == 2: #submenu_2
    while True:
      print(SEPARATOR)
      print('ВЫВЕСТИ ИНФОРМАЦИЮ')
      sub_choice = int(input('\n1 - Общая информация\n'
                             '2 - Вся информация\n' 
                             '0 - Назад\n'
                             'Введите номер пункта меню: '
                             ))
      if sub_choice == 1:
        print(SEPARATOR)
        print(f'       Общая информация'
              f'\nИмя:       {name}'
              f'\nВозраст:   {age}'
              f'\nТелефон:   {phone_number}'
              f'\nE-mail:    {email_address}'
              f'\nИндекс:    {index}'
              f'\nАдрес:     {address}'
              )
        
      elif sub_choice == 2:
        print(SEPARATOR)
        print(f'      Общая информация'
              f'\nИмя:       {name}'
              f'\nВозраст:   {age}'
              f'\nТелефон:   {phone_number}'
              f'\nE-mail:    {email_address}'
              f'\nИндекс:    {index}'
              f'\nАдрес:     {address}'
              '\n'
              f'\n    Информация о предпренимателе'
              f'\nОГРНИП:    {OGRNIP}'
              f'\nИНН:       {INN}'
              f'\n    Банковские реквизиты'
              f'\nР/с:       {settlement_account}'
              f'\nБанк:      {bank_of_beneficiary}'
              f'\nБИК:       {BIK}'
              f'\nК/с:       {correspondent_account}'
              )

      elif sub_choice == 0:
        break

      else:
        print('Введён некорректный пункт меню.')
     
  elif main_choice == 0:
    print('\nЗавершение работы. До свидания!')
    break 
    
  else:
    print('Введён некорректный пункт меню.')