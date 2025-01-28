
class View:

    @staticmethod
    def dispay_computers(computers):
        if not computers:
            print('компьютеров нет')
            return
        for comp in computers:
            View.display_dit(comp)

    @staticmethod
    def display_dit(computer):
        print(f'---------ID {computer.id}---------')
        print('Тип комкьютера ' + computer.type)
        print('id ' + computer.id)
        print('Mac ' + computer.mac)
        print('операционная система ' + computer.os)
        print('дата ввода в экп ' + computer.start_date)
        if computer.end_date == None:
            print('Находится в эксп')
        else:
            print('дата вывода ' + computer.end_date)
        print('------------------------------------\n')
    @staticmethod
    def error_text(text):
        return  "\033[34m{}".format(text)