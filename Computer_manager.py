from time import process_time_ns
from View import  *

class Computer_manager:
    def __init__(self):
        self.__computers=[]


    def add_comp(self,computer_inp):
        if any(comp.id==computer_inp.id for comp in self.__computers):
            raise ValueError('----------ОШИБКА 1(Такой тип данных уже существует)----------')
        else:
            self.__computers.append(computer_inp)

    def del_comp(self,computer):
        self.__computers.remove(computer)
        print('компьютер был успешно удален')
        pass


    def search_comp(self,id_comp):
        for comp in self.__computers:
            if comp.id==id_comp:
                return comp
        return None

    def upd_comp(self,computer,new_comp):

                computer.type=new_comp.type
                computer.mac=new_comp.mac
                computer.os=new_comp.os
                computer.start_date=new_comp.start_date
                computer.end_date=new_comp.end_date







    def list_comp(self):
        return self.__computers

