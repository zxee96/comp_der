from View import *


class ComputerManager:
    def __init__(self):
        self.computers = []

    def add_computer(self, computer):
        if self.find_computer(computer.id) or self.find_computer_by_mac(computer.mac):
            raise ValueError(f'Ошибка: Компьютер с ID {computer.id} или MAC {computer.mac} уже существует')
        self.computers.append(computer)

    def remove_computer(self, computer_id):
        computer = self.find_computer(computer_id)
        if computer:
            self.computers.remove(computer)
            View.show_message(f'Компьютер с ID {computer_id} удален')
        else:
            View.show_message(f'Ошибка: Компьютер с ID {computer_id} не найден')

    def find_computer(self, computer_id):
        for comp in self.computers:
            if comp.id == computer_id:
                return comp
        return None

    def find_computer_by_mac(self, mac):
        for comp in self.computers:
            if comp.mac == mac:
                return comp
        return None

    def update_computer(self, computer_id, new_data):
        computer = self.find_computer(computer_id)
        if computer:
            for key, value in new_data.items():
                setattr(computer, key, value)
            View.show_message(f'Компьютер {computer_id} обновлен')
        else:
            View.show_message(f'Ошибка: Компьютер с ID {computer_id} не найден')

    def list_computers(self):
        return self.computers
