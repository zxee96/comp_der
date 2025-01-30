class View:
    @staticmethod
    def display_computers(computers):
        if not computers:
            View.show_message('Список компьютеров пуст')
        for comp in computers:
            View.display_computer_details(comp)

    @staticmethod
    def display_computer_details(computer):
        print(
            f'ID: {computer.id}\nТип: {computer.type}\nMAC: {computer.mac}\nOS: {computer.os}\nСтарт: {computer.start_date}\nКонец: {computer.end_date or "Активен"}\n')

    @staticmethod
    def show_message(message):
        print(f'\033[34m{message}\033[0m')

