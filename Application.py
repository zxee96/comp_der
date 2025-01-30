from ComputerManager import *
from View import *
from DataHadnler import *

class Application:
    def __init__(self):
        self.manager = ComputerManager()
        self.view = View()


    def run(self):
        while True:
            command = input(
                '\nВыберите действие:\n1. Список компьютеров\n2. Найти компьютер\n3. Добавить компьютер\n4. Удалить компьютер\n5. Обновить компьютер\n6. Загрузить\n7. Сохранить\n8. Выйти\n> ')
            match command:
                case '1':
                    self.view.display_computers(self.manager.list_computers())
                case '2':
                    self.search_computer()
                case '3':
                    self.add_computer()
                case '4':
                    self.remove_computer()
                case '5':
                    self.update_computer()
                case "6":
                    self.load_data()
                case '7':
                    DataHandler.save_data(self.manager.list_computers())
                    self.view.show_message('Данные сохранены')
                case '8':
                    break
                case _:
                    self.view.show_message('Ошибка: Неверная команда')

    def load_data(self):
        self.manager.computers = DataHandler.load_data()

    def search_computer(self):
        computer_id = input('Введите ID: ')
        computer = self.manager.find_computer(computer_id)
        if computer:
            self.view.display_computer_details(computer)
        else:
            self.view.show_message('Компьютер не найден')

    def add_computer(self):
        data = {
            'type': input('Тип устройства: '),
            'id': input('ID (4 цифры): '),
            'mac': input('MAC (XX:XX:XX:XX:XX:XX): '),
            'os': input('ОС: '),
            'start_date': input('Дата начала эксплуатации (YYYY-MM-DD или DD.MM.YYYY): '),
            'end_date':  None
        }
        try:
            self.manager.add_computer(Computer(**data))
        except ValueError as e:
            self.view.show_message(str(e))

    def remove_computer(self):
        computer_id = input('Введите ID: ')
        self.manager.remove_computer(computer_id)

    def update_computer(self):
        computer_id = input('Введите ID: ')
        computer = self.manager.find_computer(computer_id)
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
                            user_izmena = input(
                                f'введите новое значение параметра \nпредыдущее значение параметра:{computer.type}  \n')
                            computer.type = user_izmena
                            print('параметр успешно добавлен')
                        case '2':
                            user_izmena = input(
                                f'введите новое значение параметра \nпредыдущее значение параметра:{computer.mac}  \n')
                            computer.mac = user_izmena
                            print('параметр успешно добавлен')
                        case '3':
                            user_izmena = input(
                                f'введите новое значение параметра \nпредыдущее значение параметра:{computer.os}  \n')
                            computer.os = user_izmena
                            print('параметр успешно добавлен')
                        case '4':
                            user_izmena = input(
                                f'введите новое значение параметра \nпредыдущее значение параметра:{computer.start_date}  \n')
                            computer.start_date = user_izmena
                            print('параметр успешно добавлен')
                        case '5':
                            user_izmena = input(
                                f'введите новое значение параметра \nпредыдущее значение параметра:{computer.end_date}  \n')
                            computer.end_date = user_izmena
                            print('параметр успешно добавлен')
                        case _:
                            print('такого пр-тра нет')
                case '2':
                    type = input('введите тип устройства')
                    id = computer.id
                    mac = input('введите MAC адрес компьютера')
                    os = input('введите операционную систему')
                    start_date = input('введите дату ввода в ксплоатацию')
                    end_date = input('введите дату ввода в окончания')

                    new_comp = Computer(type, id, mac, os, start_date, end_date)
                    self.manager.upd_comp(computer, new_comp)
        else:
            self.view.show_message('Компьютер не найден')

            return
