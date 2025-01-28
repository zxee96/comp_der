from Computer_manager import *
from View import *
from Computer import *
from Data_handller import *
from  Computer_manager import *
class Application:
    def __init__(self):
        self.manager=Computer_manager()
        self.view=View()
        self.data_handller=Data_handller


    def run(self):
        while True:
            print('''Доступные команды:
                     1.Список всех компьютеров
                     2.Найти компьютер по id
                     3.Добавить компьютер
                     4.Удалить компьютер
                     5.Обновить компьютер
                     6.Сохранить данные
                     7.Загрузить
                     8.Выход''')
            comand=input('Введите номер команды:')
            match comand:
                case '1':
                    self.view.dispay_computers(self.manager.list_comp())
                case '2':
                    id_comp=input('Введите id компьютреа')
                    computer=self.manager.search_comp(id_comp)
                    if computer:
                        self.view.display_dit(computer)
                    else:
                        print('Компьютер не найдем')
                case '3':
                    try:
                        type = input('введите тип устройства')
                        id = input('введите id устройства')
                        mac = input('введите MAC адрес компьютера')
                        os = input('введите операционную систему')
                        start_date = input('введите дату ввода в ксплоатацию')

                        computer=Computer(type,id,mac,os,start_date)
                        self.manager.add_comp(computer)
                    except ValueError as e:
                        print(e)

                case '4':
                     id_comp = input('Введите id компьютреа')
                     computer = self.manager.search_comp(id_comp)
                     if computer:
                         self.manager.del_comp(computer)
                     else:
                         print('Компьютер не найдем')
                case '5':
                    id_comp = input('Введите id компьютреа')
                    computer = self.manager.search_comp(id_comp)
                    if computer:
                        user_anser = input('введите комнманду\n 1.модифицировать параментр\n 2.модифицировать все \n ')
                        match user_anser:
                            case '1':
                                user_par = input('введите точное название параметра который хотите заменить:'
                                                 '\n1-devays_type,'
                                                 '\n2-mac_key,'
                                                 '\n3-system_key,'
                                                 '\n4-start_key,'
                                                 '\n5-end_key\n')
                                match user_par:
                                    case '1':
                                        user_izmena = input(f'введите новое значение параметра \nпредыдущее значение параметра:{computer.type}  \n')
                                        computer.type = user_izmena
                                        print('параметр успешно добавлен')
                                    case '2':
                                        user_izmena = input(f'введите новое значение параметра \nпредыдущее значение параметра:{computer.mac}  \n')
                                        computer.mac = user_izmena
                                        print('параметр успешно добавлен')
                                    case '3':
                                        user_izmena = input(f'введите новое значение параметра \nпредыдущее значение параметра:{computer.os}  \n')
                                        computer.os = user_izmena
                                        print('параметр успешно добавлен')
                                    case '4':
                                        user_izmena = input(f'введите новое значение параметра \nпредыдущее значение параметра:{computer.start_date}  \n')
                                        computer.start_date = user_izmena
                                        print('параметр успешно добавлен')
                                    case '5':
                                        user_izmena = input(f'введите новое значение параметра \nпредыдущее значение параметра:{computer.end_date}  \n')
                                        computer.end_date = user_izmena
                                        print('параметр успешно добавлен')
                                    case _:
                                        print('такого пр-тра нет')
                            case '2':
                                type = input('введите тип устройства')
                                id= computer.id
                                mac = input('введите MAC адрес компьютера')
                                os = input('введите операционную систему')
                                start_date = input('введите дату ввода в ксплоатацию')
                                end_date = input('введите дату ввода в окончания')

                                new_comp=Computer(type,id,mac,os,start_date,end_date)
                                self.manager.upd_comp(computer,new_comp)

                    else:
                        print('Компьютер не найдем')
                case '6':
                    self.data_handller.save_data(self.manager.list_comp())
                case '7':
                    self.data_handller.load_data(self.manager.list_comp())

                case '8':
                    break
                case _:
                     print('Не корректный ввод')



