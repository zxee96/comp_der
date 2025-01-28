class Computer:
    def __init__(self,type,id,mac,os,start_date,end_date=None):
        self.type=type
        self.id=id
        self.mac=mac
        self.os=os
        self.start_date=start_date
        self.end_date=end_date

    def todickt(self):
        return {"devays_type":self.type,
              "id_key":self.id,
              "mac_key":self.mac,
              "system_key":self.os,
              "start_key":self.start_date,
              "end_key":self.end_date}
    @staticmethod
    def fromdict(data):
        return Computer(type=data["devays_type"],
                        id=data["id_key"],
                        mac=data["mac_key"],
                        os=data["system_key"],
                        start_date=data['start_key'])
