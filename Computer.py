import re
from datetime import datetime

class Computer:
    def __init__(self, type: str, id: str, mac: str, os: str, start_date: str, end_date: str = None):
        self.type = type
        self.id = self.format_id(id)
        self.mac = self.format_mac(mac)
        self.os = os
        self.start_date = self.format_date(start_date)
        self.end_date = self.format_date(end_date) if end_date else None

    def to_dict(self):
        return {
            'type': self.type,
            'id': self.id,
            'mac': self.mac,
            'os': self.os,
            'start_date': self.start_date,
            'end_date': self.end_date
        }

    @staticmethod
    def from_dict(data):
        return Computer(**data)

    @staticmethod
    def format_id(raw_id):
        match = re.match(r'\d{4}', raw_id)
        return match.group(0) if match else '0000'

    @staticmethod
    def format_mac(raw_mac):
        clean_mac = re.sub(r'[^0-9A-Fa-f]', '', raw_mac.upper())
        if len(clean_mac) == 12:
            formatted_mac = []
            for i in range(0, 12, 2):
                formatted_mac.append(clean_mac[i:i + 2])
            return ':'.join(formatted_mac)
        return '00:00:00:00:00:00'

    @staticmethod
    def format_date(raw_date):
        for fmt in ('%Y-%m-%d', '%d.%m.%Y'):
            try:
                return datetime.strptime(raw_date, fmt).strftime('%Y-%m-%d')
            except ValueError:
                continue
        return datetime.now().strftime('%Y-%m-%d')

