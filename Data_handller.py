from Computer import *
import json
class Data_handller:
    FILE_NAME='data.json'

    @staticmethod
    def load_data(computers):
        with open(Data_handller.FILE_NAME,'r') as file:
            data=json.load(file)
            for item in data:
                computer=Computer.fromdict(item)
                computers.append(computer)


    @staticmethod
    def save_data(computers):
        data=[comp.todickt() for comp in computers]
        vibor = input('1.Хотите добавить в текущее\n2.Хотите создать новое\n')
        match vibor:
            case '1':
                with open(Data_handller.FILE_NAME, 'a') as file:
                    json.dump(data, file, indent=4)
                Data_handller.__merge_json()
                Data_handller.__remove_duplicates()
            case '2':
                with open(Data_handller.FILE_NAME, 'w') as file:
                    json.dump(data, file, indent=4)
                Data_handller.__remove_duplicates()
            case _:
                print('некоректный ввод')

    @staticmethod
    def __merge_json():
        with open(Data_handller.FILE_NAME,'r') as file:
            raw_data=file.read()
        fixed_data=raw_data.replace('][',',')
        json_data=json.loads(fixed_data)
        with open(Data_handller.FILE_NAME,'w') as file:
            json.dump(json_data,file,indent=4)


    @staticmethod
    def __remove_duplicates():
        with open(Data_handller.FILE_NAME,'r') as file:
            data=json.load(file)
        unic_records = {}
        for rec in data:
            key=rec['id_key']
            unic_records[key]=rec
        clind_data=list(unic_records.values())
        with open(Data_handller.FILE_NAME, 'w') as file:
            json.dump(clind_data, file, indent=4)